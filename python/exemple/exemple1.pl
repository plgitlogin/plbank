# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
# la ligne suivante est nécessaire pour faire appel à la fonction grade.
template=/python/function/functiongradertemplate.pl

title=exemple1.pl
text==
Ecrire deux lignes de code permettant d'initialiser les variables //hauteur// avec 1.33 et //largeur// avec 2.2 .


==
code==
# Veuillez saisir votre code ici
==
grader==
# la variable suivante contient le code de test a réaliser pour vérifier le code 
# la syntaxe est celle de doctest https://docs.python.org/3.5/library/doctest.html
__doc__="import student # le code a tester 
>>>hauteur
1.33 # le premier test 
>>>largeur
2.2
" # fin de la définition du test 
# import de la fonction d'évaluation 
from functiongrader import grade
# réalisation du test et création du json nécessaire comme sortie du l'executeur 
grade()
==
