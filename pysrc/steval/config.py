#! /usr/bin/env python3
"""
Configuration information for the bench runner

@author: chilowi at u-pem.fr
"""

from steval.testbench.testbench import EchoTestBench
from steval.testbench.python.pytest import PythonTestBench
from steval.testbench.exec.exectest import ExecutableTestBench
from steval.executor.sandbox.sandbox import Sandbox

# We define here all the configured benchs
BENCHS = {
	"echo": EchoTestBench, # a tester that does nothing else than printing the supplied dictionary
	"exec": ExecutableTestBench, # a tester based on a supplied executable (typically a script)
	"python": PythonTestBench # a tester for Python functions using annotations
}

"""
Note: the exec bench is dangerous since any executable can be run without restriction.
Currently defined sandboxes are too restrictive to run any executable.
It is recommended to wrap the testbench script in a specially crafted sandbox
authorizing appropriate syscalls for the wished use.
"""

# We define here the configured sandboxes
SANDBOXES = {
	"unlimited": Sandbox(enabled=False),
	"50M-10s": Sandbox(enabled=False, memory_limit=50 * 10**6, cpu_limit=10000),
	"seccomp-50M-10s": Sandbox(enabled=True, memory_limit=50 * 10**6, cpu_limit=10000)
}

DEFAULT_SANDBOX = "seccomp-50M-10s"

MAX_OUTPUT_SIZE = 2**16 # maximal output of the bench (in bytes)
