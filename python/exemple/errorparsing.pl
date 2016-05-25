# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=errorparsing.pl
tag=root # N'oubliez pas de remplir ce champs svp
template=/python/function/functiongradertemplate
text==

MODIFIER

==

code==
def XXXX():
	return
==

grader==
__doc__=""">>> from student import XXXX
>>> XXXX()
>>>
"""
from functiongrader import grade
grade()
==

# f i l e s=@/python/pahtdufichier/nomdufichier
soluce==
# une solution de l'exercice
# utile pour les tests
==
