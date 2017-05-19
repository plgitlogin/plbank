# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=distance2.pl
title=   Distance de Mots
tag=  # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate
text==
Il est possible de définir de nombreuses distances entre mots.

la plus simple est de simplement comparer les longeurs. 

Ecrivez une fonction hamming(mot1,mot2) qui retourne la différence des longeur.

	Quelques remarques :
		la distance est toujours positive.
		la distance entre "axxx" et "xxxb" est de 4, aucune lettre identique a une position donnée.
		la distance entre "xxxa" et "xxxb" est de 1, une seule erreur.
		la distance entre "DEMAIN" et "HIER" est de None.

==

# Choisir pltest ou soluce ou expectedoutput

pltest==
>>> hamming("xaxx","xbxx") # substitution 
1
>>> hamming("axxxa","xxx") # delete en premier en dernier
None
>>> hamming("xxx","axxxa") # insert en premier en dernier
None
>>> hamming("abaculexxxx","xxxxabacule")
11
==

