
# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title= autofunctiongradertemplate.pl
text==

Ceci est un texte qui ne devrai pas apparaitre voyez avec dr@univ-mlv.fr
en signalant le nom de l'exercice qui devrai être diférent de autogradertemplate.pl

==


files=@/python/exemple/pldoctest.py
files=@/python/exemple/pldicjson.py
files=@/python/exemple/autograder.py


code==
# Veuillez saisir votre code ici
def nomdaelafonction(n):
	pass

==

pltest==
>>> print(" ERREUR PLATEFORM ") # ERREUR PLATEFORME TEST NON Défini 
>>> True # Veuillez modifier votre exercice en ajoutant une balise pltest 
>>>
==


grader==
from autograder import autograde
autograde()
==
