# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=while 
title=   # N'oubliez pas de remplir ce champs svp
tag=while|boucle|exposant  # N'oubliez pas de remplir ce champs svp
template=/python/0PLG/template.pl
text==

# While 

Modifier le code suivant pour qu'il affiche les 20 premiers termes de la suite (1,-1,2,-2,3,-3,etc).

==

code==

i=0
while i < 10:
	print(i)
	i=i+1
print('fini')

==

expectedoutput==
1
-1
2
-2
3
-3
4
-4
5
-5
6
-6
7
-7
8
-8
9
-9
10
-10
fini
==


