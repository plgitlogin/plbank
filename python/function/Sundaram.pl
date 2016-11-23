# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Sundaram
title= Sundaram  # N'oubliez pas de remplir ce champs svp
tag=def|parameters|return # N'oubliez pas de remplir ce champs svp
template=/python/template.pl
text==
## Crible de Sundaram

Découvert en 1934 par le Mathématicien Indien S.P. Sundaram ce crible permet de trouvez des nombres premiers inférieurs a un certain seuil. Les nombres premier sont ceux de la forme 2k+1 ou k n'est pas solution d'une équation i+j+2*ij avec i et j entiers. 

On cherche les nombre premiers inférieurs à une certaine valeur n.

Trois étapes:
1) créez une liste d'entiers de 1 à n. Ecrivez la fonction **createlist** qui retourne cette liste.

	>>> createlist(5)
	[1, 2, 3, 4, 5]

2) Eliminer de la liste tout les entiers de la forme i+j+2ij ou 0<i<=j<=n . Créez une fonction **crible1** qui prend une liste en parametre et qui fait cette élimination.

	>>> crible1([1,2,3,4,5,6,7,8])
	[1, 2, 3, 5, 6, 8]

3) Ecrire une fonction **crible2** qui prend en parametre une liste et qui retourne une liste ou tout les entiers de la liste ont été transformés par la formule 2i+1 :

	>>> crible2([1,2,3,5,6,8])
	[3, 5, 7, 11, 13, 17]

==

# Choisir pltest ou soluce ou expectedoutput
# 14041997
pltest==
>>> createlist(5)
[1, 2, 3, 4, 5]
>>> crible1([1,2,3,4,5,6,7,8])
[1, 2, 3, 5, 6, 8]
>>> crible2([1,2,3,5,6,8])
	[3, 5, 7, 11, 13, 17]
>>> crible2(crible1(createlist(100)))
[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 201]
==


testcode==
def createlist(n):
	return  [x + 1 for x in range(n)]
	# return "["+"".join(range(1,n+1))+"]"

def crible1(li):
	for i in range(1,len(li)+1):
		for j in range(i,len(li)+1):
			if i+j+2*i*j < li[-1]:
				li[i+j+2*i*j -1]=0
	return [x for x in li if x !=0 ]

def crible2(l):
	return [2*x+1 for x in l]
==
