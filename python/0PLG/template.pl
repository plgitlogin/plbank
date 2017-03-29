# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>

# using the new plgrader 

name=  python/0PLG/template.pl

grader==
from plgrader import Grader
g=Grader()
print(g.grade())
==
files=@/pysrc/src/plgrader.py
files=@/pysrc/src/feedback.py
