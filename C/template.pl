# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>

# this is the template for C language
# and expectoutput
language=C

name=  Premier Langage Exercices de C

debug=on

grader==
from Cutils import grade
grade()
==
files=@/pysrc/src/Cutils.py
files=@/pysrc/src/utils.py
files=@/pysrc/src/pldoctest.py
files=@/pysrc/src/pleval.py
files=@/pysrc/src/plutils.py
#files=@/pysrc/src/student.c

before==
#include <stdio.h>
int main()
{
#line 0 "Votre Code"
==

after==
}
==
