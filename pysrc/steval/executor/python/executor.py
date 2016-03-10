#! /usr/bin/env python3
"""
Execute a Python module and save some properties about it

@author: chilowi at u-pem.fr
"""

from .codemetrics import CodeMetrics
from .memoryfiles import VirtualFileManager
from steval.utils import PrefixMapping, limited_sys, get_traceback_str, update_dict

import time, ast, sys, io, resource
from .importinfo import get_transitive_import_dependencies, RemoteDependency
from collections import namedtuple, OrderedDict

globalvars = globals

from ctypes import pythonapi, POINTER, py_object

_get_dict = pythonapi._PyObject_GetDictPtr
_get_dict.restype = POINTER(py_object)
_get_dict.argtypes = [py_object]
del pythonapi, POINTER, py_object

def dictionary_of(ob):
	dptr = _get_dict(ob)
	return dptr.contents.value
	
	
class ForeignCodeException(Exception):
	"""An exeption due to foreign code"""
	def __init__(self, cause, trace):
		self.cause = cause
		self.trace = trace
	@property
	def verbose_traceback(self):
		return get_traceback_str(self.trace)
	@classmethod
	def create(cls):
		(type, value, traceback) = sys.exc_info()
		return cls(value, traceback)

class ParsingException(ForeignCodeException):
	@property
	def explanation(self):
		if isinstance(self.cause, SyntaxError):
			return "{} detected at line {} character {}: {}".format(type(self.cause).__name__, self.cause.lineno, self.cause.offset, self.cause.text)
		else:
			return "Code parsing failed with the exception {}\n\nTraceback:\n{}".format(self.cause, self.verbose_traceback)
	def __str__(self):
		return self.explanation
		
class FailedImportException(ForeignCodeException):
	def __init__(self, rejected_imports):
		super(FailedImportException, self).__init__(None, None)
		self.rejected_imports = rejected_imports
	@property
	def explanation(self):
		return "The following imported modules were rejected (due to unavailability or blacklisting): {}".format(",".join(map(str, self.rejected_imports)))
	def __str__(self):
		return self.explanation
	
class ExecutionException(ForeignCodeException):
	@property
	def explanation(self):
		return "Code execution failed with the exception {}\n\nTraceback:\n{}".format(self.cause, self.verbose_traceback)
	def __str__(self):
		return self.explanation

class ExecutionResult(object):
	def __init__(self):
		self.executed = False
		self.result = None # could be also an exception
		self.globals = None
		self.stdout = None
		self.stderr = None
		self.handled_files = None
		self._start_time = None
	def _signal_parse_error(self, error):
		self.exception = ParsingException(error)
	def _start(self):
		self._start_time = time.process_time()
	def _end(self, result, globals=None):
		self.executed = True
		self.time = time.process_time() - self._start_time if self._start_time else None
		self.result = result
		self.globals = globals
	def __repr__(self):
		return "result={}, exception={}, stdout={}, stderr={}, files={}, time={}".format(self.result, self.exception, self.stdout, self.stderr, self.handled_files, self.time)
	def to_dict(self):
		return {"result": self.result, "globals": self.globals, "stdout": self.stdout, "stderr": self.stderr, "files": self.handled_files, "time": self.time}
		
class ExecutionEnvironment(object):
	def __init__(self):
		self.result = ExecutionResult()
		self.file_manager = VirtualFileManager()
		self._redirect_stdfiles = False
	def _execute(self):
		raise NotImplementedError()
	def execute(self):
		stdout, stderr = (sys.stdout, sys.stderr)
		try:
			if self._redirect_stdfiles:
				sys.stdout, sys.stderr = (io.StringIO(), io.StringIO())
			self._execute()
			if self._redirect_stdfiles:
				self.result.stdout = sys.stdout.getvalue().strip()
				self.result.stderr = sys.stderr.getvalue().strip()
				self.result.handled_files = {k: v.getvalue() for (k, v) in self.file_manager.created_files.items() }
			return self.result
		finally:
			sys.stdout, sys.stderr = (stdout, stderr) # restore old stdout and stderr
		
	
class ExecutionProfile(object):
	"""A restricted Python execution profile based on bultins and module whitelists"""
	def __init__(self):
		self._builtin_import = __import__
	def get_builtins_whitelist(self):
		"""Return a set of authorized builtins"""
		raise NotImplementedError()
	def get_modified_builtins(self):
		"""Return rewritten builtins limiting security risks"""
		return {}
	def get_modules_whitelist(self):
		"""Return a set of authorized modules (as strings)"""
		raise NotImplementedError()
	def get_modified_modules(self):
		"""Return the modules that have been modified to limit permissions"""
		return {}
	def get_available_files(self):
		return frozenset()
	def _import_interceptor(self, context, name, globals=None, locals=None, fromlist=(), level=0):
		"""Implementation of an import interceptor"""
		if name in self.get_modified_modules():
			return self.get_modified_modules()[name]
		elif name not in self.get_modules_whitelist():
			if name in context.imported:
				return context.imported[name]
			name2 = name.replace(".", "/")
			if name2 in context.file_manager.supplied_files:
				# special import from the supplied files
				with context.file_manager.open(name, "r") as f:
					module = object()
					exec(f.read(), module.__dict__)
					context.imported[name] = module
					return module
			else:
				raise ImportError("The module {} is not whitelisted".format(name))
		else:
			return self._builtin_import(name, globals, locals, fromlist, level)
	def make_builtins(self, file_manager):
		used = filter(lambda x: x in self.get_builtins_whitelist(), __builtins__)
		modified = self.get_modified_builtins()
		new_builtins = {k: modified[k] if k in modified else __builtins__[k] for k in used}
		class ImportContext(object):
			def __init__(self):
				self.file_manager = file_manager
				self.imported = {}
		import_context = ImportContext()
		def imp(name, globals=None, locals=None, fromlist=(), level=0):
			return self._import_interceptor(import_context, name, globals, locals, fromlist, level)
		new_builtins["__import__"] = imp
		# Reduce introspection capabilities
		from types import FunctionType
		type2 = dictionary_of(type)
		if "__bases__" in type2: type2.pop("__bases__") # to avoid climbing to the ancestor of a class
		if "__subclasses__" in type2: type2.pop("__subclasses__") # to avoid descending to the subclasses
		if "func_code" in dictionary_of(FunctionType): dictionary_of(FunctionType).pop("func_code")
		# add a specially crafted open function that preload files and store them in memory
		new_builtins["open"] = file_manager.open
		return new_builtins
	def evaluate(self, code, file_manager=None, globals=None):
		"""Evaluate some code using the current profile"""
		g = dict(globals) if globals else {} # copy the globals dictionary to not modify it in place
		g["__builtins__"] = self.make_builtins(file_manager)
		return eval(code, globals=g)
	
		
class DefaultExecutionProfile(ExecutionProfile):
	"""A default implementation of an execution profile with reasonable settings
	to try to limit execution risks"""
	def __init__(self):
		super(DefaultExecutionProfile, self).__init__()
		self.builtins_whitelist = set([
			"abs", "all", "any", "ascii", "bin", "bool", "bytearray", "bytes", "callable", "chr", "classmethod",
			"complex", "delattr", "dict", "divmod", "enumerate", "filter", "float", "format", "frozenset", "getattr",
			"globals", "hasattr", "hash", "help", "hex", "id", "input", "int", "isinstance", "issubclass", "iter",
			"len", "list", "locals", "map", "memoryview", "min", "next", "object", "oct", "open", "ord", "pow",
			"print", "property", "range", "repr", "reversed", "round", "set", "setattr", "slice", "sorted",
			"staticmethod", "str", "sum", "super", "tuple", "type", "vars", "zip",
			"None", "NotImplemented", "Ellipsis",
			"Exception", "RuntimeError", "SyntaxError", "ZeroDivisionError", "TypeError",
			"IndexError", "NameError", "AssertionError", "ImportError", "OverflowError", "LookpError",
			"IOError", "FloatingPointError", "ValueError", "UnicodeError", "ArithmeticError", "UnboundLocalError",
			"IndentationError", "UnicodeEncodeError", "KeyError",
			"sys"])
		self.modules_whitelist = set([
			"abc", "array", "base64", "binascii", "binhex", "bisect",
			"calendar", "cmath", "collections", "copy", "datetime", "decimal", 
			"difflib", "encodings", "fractions", "functools", "hashlib", "heapq",
			"math", "numbers", "operator", "queue", "random", "re", "string", "time"])
		self.modified_modules = {"sys": limited_sys}
		self.file_manager = VirtualFileManager()
	def get_builtins_whitelist(self):
		return self.builtins_whitelist
	def get_modules_whitelist(self):
		return self.modules_whitelist
	def get_modified_modules(self):
		return self.modified_modules
			
		
class CodeExecutionEnvironment(ExecutionEnvironment):
	"""Execute top-level Python code"""
	@classmethod
	def from_file(self, filepath):
		with open(filepath, "r") as f:
			return CodeExecutionEnvironemnt(f.read())
	def __init__(self, code, basedir=".", profile=DefaultExecutionProfile(), globals=None):
		super(CodeExecutionEnvironment, self).__init__()
		self.code = code
		self.profile = profile
		self.basedir = basedir
		self.ast = None
		self.metrics = None
		self.globals = {} if globals is None else globals
		self.globals["__builtins__"] = profile.make_builtins(self.file_manager)
		self.parsed = False # parsed state
	def parse(self):
		try:
			self.ast = ast.parse(self.code)
		except:
			self.result._end(ParsingException.create())
		else:
			self.metrics = CodeMetrics(self.code, self.ast)
			imports = get_transitive_import_dependencies(self.code, paths=("."))
			remote_imports = filter(lambda x: isinstance(x, RemoteDependency), imports)
			whitelisted_prefixes = PrefixMapping(map(lambda x: x.split("."), self.profile.get_modules_whitelist()))
			rejected_imports = frozenset(filter(lambda x: len(whitelisted_prefixes[x.module.split(".")]) == 0, remote_imports))
			self.rejected_imports = rejected_imports
			if not rejected_imports:
				for remote_import in remote_imports:
					__import__(remote_import)
			else:
				self.result._end(FailedImportException(rejected_imports))
		self.parsed = True
	@property
	def valid(self):
		return self.parsed is True and not isinstance(self.result.result, ForeignCodeException)
	def _execute(self):
		if not self.parsed:
			self.parse()
		if self.valid:
			g = dict(self.globals)
			self.result._start()
			try:
				exec(self.code, g)
			except Exception as e:
				self.result._end(ExecutionException.create())
			else:
				self.result._end(None, globals={k: g[k] for k in g if k not in self.globals})
			return self.result
	def execute_function(self, name, *kargs, **kwargs):
		if not self.result.executed:
			self.execute()
		function = self.result.globals.get(name)
		if function is None:
			return None
		env = FunctionExecutionEnvironment(self, name, *kargs, **kwargs)
		env.execute()
		return env.result
	
class FunctionExecutionEnvironment(ExecutionEnvironment):
	def __init__(self, parent, function, *kargs, **kwargs):
		 super(FunctionExecutionEnvironment, self).__init__()
		 self.parent = parent # parent execution environment
		 self.function = function
		 self.kargs, self.kwargs = (kargs, kwargs)
	def _execute(self):
		"""Execute the function"""
		# TODO: memory profiling..
		# Create the string to be evaluated
		args_dict = OrderedDict()
		update_dict(args_dict, [ ("kargs_{}".format(i), self.kargs[i]) for i in range(0, len(self.kargs)) ])
		update_dict(args_dict, [ ("kwargs_{}".format(k), v) for (k, v) in self.kwargs.items() ]) 
		call = "{}({})".format(self.function, ",".join(args_dict))
		self.result._start()
		globals = dict(self.parent.result.globals)
		globals.update(args_dict)
		try:
			r = eval(call, globals)
		except Exception as e:
			r = ExecutionException.create()
		self.result._end(r)
	
	
if __name__ == "__main__":
	test_code = """
import sys

def fib(n):
	return fib(n-1) + fib(n-2) if n > 1 else 1
print("Little message on stdout", file=sys.stdout)
print("Little message on stderr", file=sys.stderr) # FIXME: file
"""
	test_code2 = """
import sys

def fib(n):
	if n < 2: return 1
	v, w = (1, 1)
	for k in range(2, n+1):
		tmp = w
		w = v + w
		v = tmp
	return w
"""
	cee = CodeExecutionEnvironment(test_code)
	cee.parse()
	if cee.parsed is True:
		print("Vocabulary: {}".format(cee.metrics.vocabulary))
		print("AST height: {}".format(cee.metrics.height))
	else:
		print("Parsing error: {}".format(cee.parsed))
	with Sandbox(10000000, 10, enabled=False):
		print("foo")
		cee.execute()
		print("Result: {}".format(cee.result))
		for a in (1,2,3,4,5, 6, 7, 8, 9, 10):
			print(cee.execute_function("fib", a).result)
		ExecutionEnvironments(test_code, test_code2).test_results("fib", *[ (x,) for x in range(0, 10) ])
	print("The end.")
