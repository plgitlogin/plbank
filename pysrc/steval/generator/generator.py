#! /usr/bin/env python3
"""
An assignment generator loading PL files as dictionaries

@author: chilowi at u-pem.fr
"""

from steval.utils import compute_relpath
from steval.executor.sandbox.sandbox import Sandbox

import os, sys, re, json
from collections import OrderedDict

class DictionaryLoader(object):
	"""
	Format of the file (list of key-value entries):
	`key=value` for a single line entry
	`key==line1\nline2\n...\n==` for a multiline entry
	""" 
	def load_file(self, filepath, root_directory):
		working_directory = os.path.dirname(filepath)
		with open(filepath) as f:
			return self.load(f.read(), working_directory, root_directory)
	def load(self, content, working_directory=None, root_directory=None):
		# parsing the PL file
		regex = re.compile("^([^=]+)=(.*)$", re.M)
		regex2 = re.compile("^==$", re.M)
		d = OrderedDict()
		go = True
		offset = 0
		while go:
			m = regex.search(content, offset)
			if m:
				name = m.group(1)
				value = m.group(2)
				if value.startswith("@"):
					# Include the content of a file
					value = self.load_file(compute_relpath(root_directory, working_directory, value[1:]), root_directory)
					offset = m.end()
				elif value.startswith("="):
					# Multiline value
					m2 = regex2.search(content, m.end()+1)
					if m2:
						value = content[m.start(2) + 1: m2.start()].strip()
						offset = m2.end()
					else:
						value = content[m.start(2) +1:]
						offset = len(content)
				else:
					offset = m.end()
				d[name] = value
			else:
				go = False
		return d
		
class DictionaryTransform(object):
	def __init__(self):
		pass
	def transform(self, data):
		raise NotImplementedError()		

class DictionaryInheriter(object):
	"""
	A transform exploiting inheritance
	"""
	def transform(self, data):
		if "template" in data:
			data2 = OrderedDict(self.transform(data["template"]))
			for (k, v) in data.items():
				if k != "template":
					data2[k] = v
			return data2
		else:
			return data # do nothing
			
class DictionarySubstituer(DictionaryTransform):
	"""
	A transform substituting variables
	"""
	DEFAULT_MEMORY_LIMIT = 10000000 # in bytes
	DEFAULT_CPU_LIMIT = 500 # in milliseconds
	def transform(self, data):
		if "substituer" in data:
			return self.substitute(data, re.compile(data["substituer"]), data.get("precode", None))
		else:
			return data
	def substitute(self, data, substituer, precode):
		"""Use a sandbox for the substitution"""
		sandbox = Sandbox(memory_limit=50000000, cpu_limit=500, enabled=True)
		try:
			return sandbox.eval(self._substitute, data, substituer, precode)
		except Exception as e:
			raise Exception("Sandboxed substitution failed", e)
	def _substitute(self, data, substituer, precode):
		"""This method should always be called in a sandbox since we evaluate Python code from foreign sources"""
		data2 = OrderedDict()
		if precode:
			exec(precode, data2)
		for (k, v) in data.items():
			if k in ("substituer", "precode"): continue
			v2 = ""
			i = 0
			for m in substituer.finditer(v):
				v2 += v[i:m.start()]
				r = str(eval(m.group(1), data2))
				v2 += r
				i = m.end()
			v2 += v[i:]
			data2[k] = v2
		return data2
		
def load_dictionary(filepath, root=None):
	"""Default method to load a dictionary using the standard chain: 
	loader, inheriter and substituer"""
	if root is None:
		# is there a double slash in the filepath to mark the root directory?
		i = filepath.find("//")
		if i:
			root = filepath[0:i]
		else:
			root = os.path.dirname(filepath)
	d = DictionaryLoader().load_file(filepath, root)
	for transform in (DictionaryInheriter().transform, DictionarySubstituer().transform):
		d = transform(d)
	return d
		
if __name__ == "__main__":
	# load the dictionary and dump it under a JSON format
	try:
		filepath = sys.argv[1]
		root = sys.argv[2] if len(sys.argv) >= 3 else None
	except:
		print("Usage: {} dictionaryFilepath [rootDirectory]".format(sys.argv[0]), file=sys.stderr)
		sys.exit(-1)
	print(json.dumps(load_dictionary(filepath, root)))
