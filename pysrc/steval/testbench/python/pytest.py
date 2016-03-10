#! /usr/bin/env python3
"""
Definition of annotations to define tests for Python functions

@author: chilowi at u-pem.fr
"""

from steval.testbench.testbench import TestStatus, TestBench, TestBenchException, CompoundTest, TestFragment, TestVerdict, SimpleTestVerdict, CompoundTestVerdict, TestVerdictConsolidator
from steval.testbench.python import generator
from steval.executor.python.executor import CodeExecutionEnvironment, ExecutionException

import inspect, re, sys

class Arguments(object):
	MAIN = object() # special object used to replace arguments for main code
	"""Arguments for a single run of the function"""
	def __init__(self, elements=tuple(), complexity=None):
		self.elements = elements
		self.complexity = complexity if complexity else {} # estimation of the complexity using different criteria
	def to_dict(self):
		return {"kargs": self.elements, "complexity": self.complexity}
		
class ResultComparator(object):
	def __call__(self, x, y):
		raise NotImplementedError()
	
class DefaultComparator(ResultComparator):
	def __call__(self, x, y):
		return x.result == y.result

class FunctionTestContext(object):
	def __init__(self, name):
		self.name = name
		self.arguments_set = []
		self.comparator = DefaultComparator()
		self.supplied_files = []
	def test_annotation(f):
		f._test_annotation = True
		return f
	@test_annotation
	def file(self, name="-"):
		"""Supply a file (by default stdin)"""
		# TODO: do not work yet...
		self.supplied_files.append(name)
	@test_annotation
	def arguments(self, *args, complexity=None):
		self.arguments_set.append(Arguments(tuple(args), complexity=complexity))
	@test_annotation
	def arguments_generator(self, generator, complexity_evaluator=None):
		for arguments in generator:
			self.arguments(*arguments, complexity=complexity_evaluator(arguments) if complexity_evaluator else None)
	@test_annotation
	def compare(self, comparator=DefaultComparator()):
		self.comparator = comparator
	@classmethod
	def annotations(cls):
		"""Return the methods that may be used to annotate functions to be tested"""
		result = []
		for (name, ann) \
		in inspect.getmembers(cls, lambda x: getattr(x, "_test_annotation", False) is True):
			result.append(name)
		return tuple(result)
	@classmethod
	def build_annotation(cls, contexts, annotation_name, mock=False):
		def ann(*kargs, **kwargs):
			def wrapper(f):
				if f.__name__ not in contexts:
					contexts[f.__name__] = cls(f.__name__)
				getattr(contexts[f.__name__], annotation_name)(*kargs, **kwargs)
				return f
			return wrapper
		def ann_mock(*kargs, **kwargs):
			return lambda x: x
		return ann_mock if mock else ann
	@classmethod
	def build_annotations(cls, contexts, mock=False):
		d = {}
		for a in cls.annotations():
			d[a] = cls.build_annotation(contexts, a, mock)
		return d

class PythonComparisonTest(CompoundTest):
	def __init__(self, reference_code, proposed_code, taboo=None):
		super(PythonComparisonTest, self).__init__()
		self.test_contexts = {}
		self.useless_test_contexts = {} # non used test contexts for proposed code
		globals = {"generator": generator}
		ref_globals = dict(globals)
		ref_globals.update(FunctionTestContext.build_annotations(self.test_contexts))
		proposed_globals = dict(globals)
		proposed_globals.update(FunctionTestContext.build_annotations(None, mock=True))
		self.reference_code = CodeExecutionEnvironment(reference_code, globals=ref_globals)
		self.proposed_code = CodeExecutionEnvironment(proposed_code, globals=proposed_globals)
		self.taboo = taboo
	def initialize(self):
		this = self
		class ParseTest(TestFragment):
			def get_precedence(self):
				return -100 #it must be the first test
			def _execute(self):
				failure = False
				r = {}
				this.reference_code.parse()
				this.proposed_code.parse()
				for e in ("reference", "proposed"):
					element = this.reference_code if e == "reference" else this.proposed_code
					if element.valid:
						r["{}CodeCompilation".format(e)] = SimpleTestVerdict(TestStatus.SUCCESS, {"explanation": "Compilation was successful"})
					else:
						failure = True
						r["{}CodeCompilation".format(e)] = SimpleTestVerdict(TestStatus.FATAL_FAILURE, 
							{"explanation": "Cannot compile code", "result": element.result.result})
				return CompoundTestVerdict(TestStatus.FATAL_FAILURE if failure else TestStatus.SUCCESS, {}, r)
		class TabooTest(TestFragment):
			def __init__(self, code, taboo):
				TestFragment.__init__(self)
				self.code = code
				self.taboo = taboo
			def get_precedence(self):
				return -99
			def _execute(self):
				taboo_cases = {}
				for t in self.taboo:
					try:
						m = re.compile(t).search(self.code, re.M)
						if m:
							taboo_cases[t] = m.group(0)
					except Exception as e:
						print(e, file=sys.stderr)
						pass # if the regular expression is invalid
				if taboo_cases:
					return SimpleTestVerdict(TestStatus.FATAL_FAILURE, {"message": "Taboo expressions were found: {}".format(",".join(taboo_cases.values()))})
				else:
					return SimpleTestVerdict(TestStatus.SUCCESS, {"message": "No taboo expression found"})
		class FunctionSingleExecutionTest(TestFragment):
			def __init__(self, name: str, comparator, arguments):
				TestFragment.__init__(self)
				self.name = name
				self.comparator = comparator
				self.arguments = arguments
				self.results = [None, None]
			def _execute(self):
				i = 0
				for code in (this.reference_code, this.proposed_code):
					if self.arguments is not Arguments.MAIN:
						self.results[i] = code.execute_function(self.name, *self.arguments.elements)
					else:
						self.results[i] = code.result
					i += 1
				verdict = self.comparator(self.results[0], self.results[1])
				if isinstance(verdict, TestVerdict):
					return verdict
				elif verdict is True:
					return SimpleTestVerdict(TestStatus.SUCCESS, {"arguments": self.arguments}, results = self.results)
				else:
					return SimpleTestVerdict(TestStatus.FAILURE, {"arguments": self.arguments, "message": str(verdict)}, results = self.results)
			@classmethod
			def get_main_test(cls, context):
				return cls(context.name, context.comparator, Arguments.MAIN)
		class FunctionMultiExecutionTest(CompoundTest):
			def __init__(self, name, comparator, arguments_set):
				super(FunctionMultiExecutionTest, self).__init__()
				self.name = name # function name
				i = 0
				for a in arguments_set:
					self.add(i, FunctionSingleExecutionTest(self.name, comparator, a))
					i += 1
			@classmethod
			def get_test(cls, context):
				return cls(context.name, context.comparator, context.arguments_set)
		class MainExecutionTest(TestFragment):
			def get_precedence(self):
				return -98
			def _execute(self):
				results = {}
				for e in ("reference", "proposed"):
					code = this.reference_code if e == "reference" else this.proposed_code 
					results["{}CodeExecution".format(e)] = code.execute()
				ref = results["referenceCodeExecution"] # reference results
				for (function_name, context) in this.test_contexts.items():
					if context.arguments_set:
						if function_name != "main":
							this.add("function_{}".format(function_name), FunctionMultiExecutionTest.get_test(context))
						else:
							# special case for main code
							this.add("main_code", FunctionSingleExecutionTest.get_main_test(context))
				verdicts = {}
				for (k, v) in results.items():
					verdicts[k] = SimpleTestVerdict(TestStatus.FATAL_FAILURE if isinstance(v.result, ExecutionException) else TestStatus.SUCCESS, v.to_dict())
				return TestVerdictConsolidator().consolidate(verdicts)
		pt = ParseTest()
		pt.execute() # preexecute parsing (outside sandbox)
		if self.taboo:
			self.add("taboo", TabooTest(self.proposed_code.code, self.taboo))
		self.add("parsing", pt)
		self.add("main", MainExecutionTest()) # should automatically add the dependent tests

class PythonTestBench(TestBench):
	def prepare(self):
		proposed = self.data.get("proposed")
		answer = self.data.get("answer")
		taboo = self.data.get("taboo")
		if taboo:
			taboo = taboo.split(",")
		if proposed is None or answer is None:
			raise TestBenchException("Missing proposed and answer keys")
		self.test = PythonComparisonTest(answer, proposed, taboo)
		self.test.initialize()
	def execute(self):
		return self.test.execute()


