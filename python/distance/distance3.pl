# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=distance3.pl
title=   Distance de HAMMING
tag=  # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate
text==

La distance de Hamming s'interresse à des mots de même longeur (durée de transmission identique).


Ecrivez une fonction hamming(mot1,mot2) qui retourne le nombre de lettre différentes dans les deux mots.

Si les mots ne sont pas de même longeur la fonction retourne None.

	Quelques exemples :
		la distance est toujours positive.
		la distance entre "axxx" et "xxxb" est de 0.
		la distance entre "xaxax" et "YYY" est de 2.
		la distance entre "DEMAIN" et "HIER" est de 2.

==

# Choisir pltest ou soluce ou expectedoutput

pltest==
>>> distanceL("xaxx","xbxx") # substitution 
0
>>> distanceL("axxxa","xxx") # delete en premier en dernier
2
>>> distanceL("xxx","axxxa") # insert en premier en dernier
2
>>> distanceL("abaculexxxx","xxxxabacule")
0
==

