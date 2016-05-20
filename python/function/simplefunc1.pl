template=/python/function/functiongradertemplate
title=simplefunc1.pl
text==
Veuiller ecrire un code qui défini une fonction //fizzbuzz(n)// qui prend en parameters un entier
et qui affiche Fizz si n est divisible par 3 et  Buzz si n est divisible par 7.
==
grader==
__doc__=""">>> from student import fizzbuzz
>>> fizzbuzz(3) # divisible par 3
'Fizz'
>>> fizzbuzz(7) # divisible par 7
'Buzz'
>>> fizzbuzz(3*7) # divisible par les deux 
'Fizz Buzz'
>>> fizzbuzz(3*7*3841) # divisible par les deux 
'Fizz Buzz'
>>> fizzbuzz(11) # ni l'un ni l'autre 
>>> 
"""
from functiongrader import grade
grade()
==



letest==
__doc__=""">>> from student import fizzbuzz
>>> fizzbuzz(3) # divisible par 3
'Fizz'
>>> fizzbuzz(7) # divisible par 7
'Buzz'
>>> fizzbuzz(3*7) # divisible par les deux 
'Fizz Buzz'
>>> fizzbuzz(3*7*3841) # divisible par les deux 
'Fizz Buzz'
>>> fizzbuzz(11) # ni l'un ni l'autre 
>>> 
"""
==
