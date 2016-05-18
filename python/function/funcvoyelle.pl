# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=funcvoyelle.pl
template=/python/function/functiongradertemplate
text==
Ecrire une fonction //voyelles// qui compte le nombre de voyelles (minuscules, sans accents) dans une chaîne de
caractères u passée en argument.

==

code==
# les voyelles aeiou

==

grader==
__doc__=""">>> from student import voyelles
>>> voyelles("aeiou")
5
>>>voyelles("ceci est un exemple")
7
>>>voyelles("")
0
>>>voyelles("zrt&(§ç&!'§(&!'è(ç")
0
"""
from functiongrader import grade
grade()
==

# files=@/python/pahtdufichier/nomdufichier
