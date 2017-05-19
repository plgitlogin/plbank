# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=distance4.pl
title=   Distance de Levenstein (d'édition)
tag=function|dynamicprogramming # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate
text==

La distance d'édition est le nombre ***minimal*** d'opérations qui permet de transformer un mots en un autre.

Dans le cas de la distance de Levenstein (Vladimir Levenshtein[https://fr.wikipedia.org/wiki/Vladimir_Levenshtein]) les opérations sont (M mot d'origine, P mot cible) :
	substitution <> d'un caractère de M en un caractère de P ;
	ajout + dans M d'un caractère de P ;
	suppression - d'un caractère de M.


Ecrivez une fonction distance_edition(mot1,mot2) qui retourne la distance d'édition entre les deu mots en paramètres.

Si les mots ne sont pas de même longeur la fonction retourne None.

Quelques exemples :
		la distance est toujours positive (ou nulle si les mots sont identiques).
		la distance entre "axxx" et "xxxb" est de 2.
		la distance entre "xaxax" et "YYY" est de 8.
		la distance entre "xaxax" et "xxx" est de 2.
		la distance entre "instance" et "distances" est de 3 (+d -n +s)

TODO la formule de récurrence (lien sur récurrence)
TODO une image du tableau a remplir (lien sur programmation dynamique)

==

# Choisir pltest ou soluce ou expectedoutput

pltest==
>>> distance_edition("xaxx","xbxx") # substitution 
0
>>> distance_edition("axxxa","xxx") # delete en premier en dernier
2
>>> distance_edition("xxx","axxxa") # insert en premier en dernier
2
>>> distance_edition("abaculexxxx","xxxxabacule")
0
==

