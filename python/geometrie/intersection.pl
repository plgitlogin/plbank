# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=intersection de deux droites
title= Intersection  # N'oubliez pas de remplir ce champs svp
tag=  # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate
text==
Ecrire une fonction **intersection(a1,b1,a2,b2)** qui retourne un tuple contenant les valeurs xi yi du point d'intersection des deux droites.

	>>> intersection(1.0,-1,0,0.0,1.0)
	2.0,1.0

Ecrire un programme qui saisi au clavier sur quatres lignes deux points et qui affiche l'équation de droite qui passe par ces deux points.

	1  0
	0  -1
	Droite d'équation y = 1.0 x + -1.0 

affiche l’équation de la droite passant par deux points P
et Q dont les coordonnées auront étée saisies au clavier.



==


pltest==
	>>> intersection(1.0,-1,0,0.0,1.0)
	2.0,1.0
==



# Choisir pltest ou soluce ou expectedoutput

