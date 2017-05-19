# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=while 
title=   # N'oubliez pas de remplir ce champs svp
tag=while|boucle  # N'oubliez pas de remplir ce champs svp
template=/python/0PLG/template.pl
text==

# While 

Modifier le code suivant pour qu'il affiche les entiers de
15 à 3 (compris) en ordre décroissant.

==

code==

i=0
while i < 10:
	print(i)
	i=i+1
print('fini')

==

expectedoutput==
15
14
13
12
11
10
9
8
7
6
5
4
3
fini
==


