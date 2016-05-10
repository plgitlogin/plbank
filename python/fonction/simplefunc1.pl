template=/python/fonction/functiongradertemplate
title=simplefunc1.pl
text==
Veuiller ecrire un code qui défini une fonction //fizzbuzz(n)// qui prend en parameters un entier
et qui affiche Fizz si n est divisible par 3 et  Buzz si n est divisible par 7.


==


files=@/python/fonction/functiongrader.py

files@=functiongrader.py

files=functiongrader.py

grader==


__doc__=""">>> from student import fizzbuzz
>>> fizzbuzz(3)
'Fizz'
>>> fizzbuzz(7)
'Buzz'
>>> fizzbuzz(33/0)
'Fizz Buzz'
>>> fizzbuzz(11)
>>> 
"""
from functiongrader import grade
grade()

==


