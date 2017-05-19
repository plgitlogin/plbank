"""
>>> f()
3
>>> f()
4
"""
from ctypes import *
cdll.LoadLibrary("./librien.so.1.0")
librien=CDLL("./librien.so.1.0")
def f():
	return librien.f()
"""
>>> f()
3
>>> f()
4
"""
