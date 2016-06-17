# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=lireunelisteint.pl
title=  Lire une liste d'entiers
tag= list|input|conversion
template=/python/exemple/autogradertemplate
text==
Nous souhaitons lire une liste d'entiers que 
nous allons suppose être entrée sur une seule ligne avec un espace entre chaque valeur de la liste.

	12 4 15 6 17 1888 0 -3 26

Nous allons réutiliser les fonctions **input** et **split** pour lire la ligne et la découper puis nous devons transformer chaque élément en entier en utilisant le opérateur de convertion **int** qui s'utilise comme une fonction.

Pour terminer l'exercice afficher simplement la somme des valeurs lues.
Pour cette liste :
	1965
==

soluce==
print(sum([int(x) for x in input().split()]))
==

inputgenerator==
l=[]
from random import randint
print(" ".join([ randint(0,2000) for j in range(randint(3,7))]))
==

feedback==
Très bien 
Retenez bien ce code :<br>
	input().split()
qui permet d'obtenir une liste à partir d'une chaine en coupant à chaque espace
	a=0
	for l in input().split():
		a += int(l)
	print(a)
==
