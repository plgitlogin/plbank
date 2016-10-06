# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Erreurs de Types 
title=  Erreur de Types 001
tag=TypeError  # N'oubliez pas de remplir ce champs svp
template=/python/IUT/template

text==

#  Erreurs de Types
Dans le code suivant il y a une erreur de compilation qui est due à un opérateur qui est utilisé avec des arguments qui sont de types incompatibles.


==


code==
# Il faut transformer l'entier (int) en chaine (str) pour que l'opérateur + fonctionne.
print(" Nombre de jours dans une semaine "+7)
# Il faut transformer la chaine en float pour que l'opération soit possible  
PI="3.14159"
print(" La circonférence d'un cercle de rayon 7 est de ",2*PI*7)
# TODO
==

expectedoutput==
 Nombre de jours dans une semaine 7
 La circonférence d'un cercle de rayon 7 est de 43.98226
==

