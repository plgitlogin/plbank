#! /usr/bin/env python3
"""
Some useful classes and functions

@author: chilowi at u-pem.fr
"""

import os, sys, io, collections, traceback
from collections import OrderedDict

class ReadOnlyDictWrapper(collections.Mapping):
	"""An immutable wrapper for a dictionary"""
	def __init__(self, data):
		self._data = data
	def __getitem__(self, key):
		return self._data[key]
	def __iter__(self):
		return iter(self._data)
	def __len__(self):
		return len(self._data)
		
class PrefixMapping(object):
	"""Query the longest prefix from the collection"""
	def __init__(self, elements):
		self._prefixes = set()
		for element in elements:
			for i in range(1, len(element)+1):
				self._prefixes.add(tuple(element[0:i]))
	def __getitem__(self, key):
		i = 0
		while i < len(key) and tuple(key[0:i+1]) in self._prefixes:
			i += 1
		return key[0:i]
		
class LimitedModule(object):
	"""A module proxy exposing only the wished members"""
	def __init__(self, module, *whitelist):
		self.module = module
		self.whitelist = whitelist
	def __getattr__(self, k):
		if k in self.whitelist:
			return getattr(self.module, k)
		else:
			raise KeyError("The member {} of the module is not in the authorized whitelist".format(k))
			
		
limited_sys = LimitedModule(sys, "stdin", "stdout", "stderr")

def compute_relpath(root, current_dir, path):
	if not root.endswith("/"): root += "/"
	root = os.path.abspath(root)
	current_dir = os.path.abspath(current_dir)
	if not current_dir.startswith(root):
		raise IOError("The current dir {} is not under the root {}".format(current_dir, root))
	if path.startswith("/"):
		path = os.path.abspath(os.path.join(root, path[1:]))
	else:
		path = os.path.abspath(os.path.join(current_dir, path))
	if not path.startswith(root):
		raise IOError("The specified path {} tries to escape from the root dir {}".format(path, root))
	return path

def get_traceback_str(trace=None):
	if trace is None:
		trace = sys.exc_info()[2]
	container = io.StringIO()
	# traceback.print_tb(trace, file=container) # FIXME: cause a problem with seccomp sandboxing
	return container.getvalue()

def jsoniblify(struct):
	"""Render a data structure jsonable"""
	if struct is None or isinstance(struct, (bool, int, float, str)):
		return struct # no modification
	elif isinstance(struct, (list, tuple)):
		return [ jsoniblify(s) for s in struct ]
	elif isinstance(struct, dict):
		d = OrderedDict()
		for (k, v) in struct.items():
			d[jsoniblify(k)] = jsoniblify(v)
		return d
	elif hasattr(struct, "to_dict"):
		return jsoniblify(struct.to_dict())
	else:
		return str(struct) # last resort: we convert to a string

def update_dict(d, entries):
	for (k, v) in entries:
		d[k] = v
	return d
