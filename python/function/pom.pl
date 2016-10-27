# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=  pom.pl
title=  Pom Pom Pom Pom  # N'oubliez pas de remplir ce champs svp
tag=  # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate
text==

Ecrire une fonction **pom** qui prend un parametre entier n et qui affiche

	Si n < 0 affiche "Pas de Pom"
	sinon affiche "Pom " pour n = 1
	      affiche "Pom Pom" pour n =2
	etc


==

pltest==
>>> pom(0)
'Pas de Pom'
>>> pom(1) # pas d'espace dans la solution 
'Pom'
>>> pom(1) # pas d'espace à la fin
'Pom'
>>> pom(12) # plein de pomme 
'Pom Pom Pom Pom Pom Pom Pom Pom Pom Pom Pom Pom'
>>> pom(-777) #vraiment négatif
'Pas de Pom'
==


