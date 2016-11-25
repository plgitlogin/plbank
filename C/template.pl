# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>

# this is the template for C language 
language=C

name=  Premier Langage Exercices de C

grader==
from Cutils import grade
grade()
==
files=@/pysrc/src/Cutils.py
files=@/pysrc/src/utils.py
files=@/pysrc/src/pldoctest.py
files=@/pysrc/src/pleval.py
