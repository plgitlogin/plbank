# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Entrée Sorties
title=   # N'oubliez pas de remplir ce champs svp
tag=input|print
template=/python/IUT/template
text==

Exercice classique d'entrée sortie. La ligne suivant permet de demander une information a l'utilisateur:

	nom = input("Comment vous appelez vous ?")

Maintenant la variable **nom** contient une chaine. 

	age =  int(input("Quel age avez vous ?"))

Ici nous avons été obligé de transformer la chaine fournie en entier pour pouvoir l'utiliser dans un calcul (par exemple l'age en mois). 

	print(" Bonjour ", nom," vous avez ",age, " ans.")

Utiliser ces informations pour écrire un code qui produit l'execution suivantes :


	Quel est votre nom ?**Eric**
	Quel est votre age ?**17**
	Bonjour  Eric  vous avez  17  ans

La partie en **gras** étant tapée par l'utilisateur.

==
code==
# Votre code 
==

soluce==
nom=input("Quel est votre nom ?")
age=int(input("Quel est votre age ?"))
print(" Bonjour ",nom," vous avez ",age," ans")

==

input==
LEPRENOM
200
==

