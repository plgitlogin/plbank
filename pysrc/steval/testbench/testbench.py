#! /usr/bin/env python3
"""
A test bench for answers submitted for a problem

@author: chilowi at u-pem.fr
"""

from enum import IntEnum
from steval.utils import get_traceback_str, jsoniblify

from collections import OrderedDict

class TestBenchException(Exception):
	"""Exception raised if there is a problem while initializing a test bench"""
	def __init__(self, message, cause=None):
		self.message = message
		self.cause = cause

class TestStatus(IntEnum):
	EXCEPTION = -1 # an exception has been encountered that is due to a problem of the testing framework
	FATAL_FAILURE = 0 # a failure that prevents other test to be done
	FAILURE = 1 # a failure that allows other tests to be made
	PARTIAL_SUCCESS = 2 # a mix of failure and success
	SUCCESS = 3 # a complete success

class TestVerdict(object):
	def __init__(self, status: TestStatus, grades: dict):
		self.status = status # the status of the test
		self.grades = grades # some free grades (numerical or textual) in a dictionary
	def to_dict(self):
		"""Convert the result to a JSONizable dictionary form"""
		return {"status": str(self.status.name).lower(), "grades": jsoniblify(self.grades)}
		
class SimpleTestVerdict(TestVerdict):
	def __init__(self, status: TestStatus, grades: dict, results=None):
		TestVerdict.__init__(self, status, grades)
		self.results = results
	def to_dict(self):
		d = super(SimpleTestVerdict, self).to_dict()
		d.update(results=jsoniblify(self.results))
		return d
		
	
class CompoundTestVerdict(TestVerdict):
	def __init__(self, status, grades, child_verdicts: dict):
		TestVerdict.__init__(self, status, grades)
		self.child_verdicts = child_verdicts
	def to_dict(self):
		d = super(CompoundTestVerdict, self).to_dict()
		d["childVerdicts"] = OrderedDict()
		for (k, v) in self.child_verdicts.items():
			d["childVerdicts"][k] = v.to_dict()
		return d
		
class TestVerdictConsolidator(object):
	def consolidate(self, verdicts: dict):
		"""Default implementation to consolidate verdicts"""
		if not verdicts:
			return None
		status = min(map(lambda x: x.status, verdicts.values()))
		grades = { k: v.grades for (k, v) in verdicts.items() }
		return CompoundTestVerdict(status, grades, verdicts)
		
		
class Test(object):
	def __init__(self):
		self._result = None
	def get_precedence(self):
		# return the precedence of the test fragment
		# a fragment with a lower precedence value will be executed first
		return 0
	def initialize(self):
		"""Initialiaze the test
		Code implemented in this method must be safe and not depend on user input (it may be executed outside of a sandbox"""
		pass
	def execute(self):
		if not self._result: 
			try:
				self._result = self._execute()
			except Exception as e:
				self._result = SimpleTestVerdict(TestStatus.EXCEPTION, {"exception": e, "exceptionTraceback": get_traceback_str()})
		return self._result
	def _execute(self):
		"""Execute the test fragment and return a TestVerdict
		Execution of this method is not generally safe since user-defined can be executed
		Execution must be sandboxed"""
		raise NotImplementedError()

class TestFragment(Test):
	pass
		
class CompoundTest(Test):
	"""A collection of test fragments"""
	def __init__(self, consolidator=TestVerdictConsolidator()):
		Test.__init__(self)
		self.children = {}
		self.consolidator = consolidator
		self._counter = 0 # counter of added tests
	def add(self, name, test: Test):
		self.children[name] = (test, self._counter)
		self._counter += 1
	def _execute(self):
		verdicts = {}
		go = True
		while go:
			start_counter = self._counter
			testnames = list(filter(lambda x: x not in verdicts, self.children))
			# sort the sub-tests to be executed, first by precedence, next by addition order
			testnames.sort(key= lambda x: (self.children[x][0].get_precedence(), self.children[x][1]))
			for testname in testnames:
				test = self.children[testname][0]
				verdicts[testname] = test.execute() # tests can add new tests to their parent
				if verdicts[testname].status in (TestStatus.EXCEPTION, TestStatus.FATAL_FAILURE):
					go = False
					break # do not continue testing
			go = go and self._counter > start_counter # new tests have been added
		return self.consolidator.consolidate(verdicts)

class TestBench(object):
	def __init__(self, data):
		self.data = data
	def prepare(self):
		"""Prepare the execution
		One must assume that the preparation is safe and never execute unknown code
		Therefore it is not sandboxed"""
		pass # do nothing by default, override this for a custom behavior
	def execute(self):
		raise NotImplementedError("should be implemented in derived classes")
		
class EchoTestBench(TestBench):
	"""A test bench that does nothing
	It prints the content of supplied dictionary in its verdict"""
	def execute(self):
		return SimpleTestVerdict(TestStatus.SUCCESS, {"echo": self.data})
