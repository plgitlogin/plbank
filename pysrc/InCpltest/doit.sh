cat >student.c <<EOF
int f(){ return 3; }
EOF
gcc  -Wall -fPIC -c student.c
gcc student.o -shared -o librien.so.1.0
cat >stub.py <<XXX
"""
>>> f()
3
>>> f()
4
"""
XXX

cat >>stub.py <<EOF
from ctypes import *
cdll.LoadLibrary("./librien.so.1.0")
librien=CDLL("./librien.so.1.0")
def f():
	return librien.f()
EOF


cat pltest >>stub.py
python3 -m doctest stub.py
