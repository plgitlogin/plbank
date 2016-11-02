
# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=functiongradertemplate.pl
text==

Ceci est un texte qui ne devrait pas apparaître voyez avec dr@univ-mlv.fr
en signalant le nom de l'exercice qui devrai être différent de functiongradertemplate.pl

This sould not happend send a email to dr@univ-mlv.fr.

==


files=@/python/exemple/pldoctest.py
files=@/python/exemple/pldicjson.py
files=@/python/function/functiongrader.py


code==
# Veuillez saisir votre code ici
def nomdaelafonction(n):
	pass

==

grader==
from pldicjson import getpldic

dic = getpldic()
dic["leteste"]
from functiongrader import grade
grade(dic["leteste"])
==
