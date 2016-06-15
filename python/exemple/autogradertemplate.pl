
# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title= python/exemple/autofunctiongradertemplate.pl
text==

Ceci est un texte qui ne devrai pas apparaitre voyez avec dr@univ-mlv.fr
en signalant le nom de l'exercice qui devrai être diférent de autogradertemplate.pl

==

# chargement des fichiers utiles 
files=@/python/exemple/pldoctest.py
files=@/python/exemple/pldicjson.py
files=@/python/exemple/autograder.py


# en fonction des balises présentes fait le bon teste
grader==
from autograder import autograde
autograde()
==
