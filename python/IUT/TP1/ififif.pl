# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Branchements
title=  if if if and else
tag=if|else|and  # N'oubliez pas de remplir ce champs svp
template=/python/IUT/template
text==

Demander un entier à l'utilisateur avec //input// puis afficher si il c'est un multiple de 2 de 3  et de 7 avec les affichages suivants.
<br>
Pour 2 <br>
Affiche :<br>
	2 est divisible par 2.
Pour 6 <br>
	6 est divisible par 2 et par 3.
Pour 42 <br>
	42 est divisible par 2 et par 3 et par 7.
Pour 17 <br>
	17 n'est divisble ni par 2 ni par 3 ni par 7.

Faites l'exercice sans utiliser les opérateurs and et or.

==

# Choisir pltest ou soluce ou expectedoutput

soluce==
X=input("Entrez un entier")
if X % 2 == 0 and X % 3 == 0 and X % 7 ==0 :
	print("%d est divisible par 2 et par 3 et par 7." % X)
if X % 2 == 0 and X % 3 != 0 and X % 7 ==0 :
	print("%d est divisible par 2 et par 7." % X)
if X % 2 == 0 and X % 3 == 0 and X % 7 !=0 :
	print("%d est divisible par 2 et par 3." % X)
if X % 2 != 0 and X % 3 == 0 and X % 7 ==0 :
	print("%d est divisible par 3 et par 7." % X)
if X % 2 != 0 and X % 3 == 0 and X % 7 !=0 :
	print("%d est divisible par 3." % X)
if X % 2 == 0 and X % 3 != 0 and X % 7 !=0 :
	print("%d est divisible par 2." % X)
if X % 2 != 0 and X % 3 != 0 and X % 7 ==0 :
	print("%d est divisible par 7." % X)
if X % 2 != 0 and X % 3 != 0 and X % 7 !=0 :
	print("%d n'est divisble ni par 2 ni par 3 ni par 7." % X)
==

input0==
2
==
input1==
6
==
input2==
42
==
input3==
17
==
input4==
14
==
input5==
77
==
input6==
69
==

taboo=and|or
