
# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=functiongradertemplate.pl
text==

Ceci est un texte qui ne devrai pas apparaitre voyer avec dr@univ-mlv.fr
en signalant le nom de l'exercice qui devrai être diférent de functiongradertemplate.pl

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
