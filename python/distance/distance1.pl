# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=distance1.pl
title=   Distance d'édition basique 
tag=function  # N'oubliez pas de remplir ce champs svp
template=/python/0PLG/template
text==

	La distance d'édition de deux mots est la plus petite distance en terme du nombre de modifications dites d'édition qui permet de passer d'un mot à l'autre.

	Cette distance est plus ou moins facile à calculer en fonction des commandes autorisées.

Pour commencer nous d'utiliserons deux opérations:
			delete (effacer un caractère)
			add (vous ajouter le caractère de votre choix).
exemple distance de toto et tata par transformation de toto en tata
	t == t passage aux deuxième caractère des deux chaines 
	a != o deux possibilités soit
		on ajoute o et l'on avance sur t et l'on reste sur a
		soit on 

	Ecrivez une fonction distance1(mot1,mot2) qui retourne la distance d'édition minimal qui permet de passer de mot1 à mot2.

	Quelques remarques :
		la distance maximale est ici ou plus de la taille des deux mots (j'efface tout mot1 et j'écrit le mot2).
		la distance d'edition entre "axxx" et "xxxb" est de 2.
		la distance d'édition entre "xaxax" et "xxx" est de 2.
		la distance d'édition entre "xxx" et "xbxbx" est de 2.

	On supposera que les mots sont "petits" et donc que l'on peut tester toutes les suites d'opérations possible.
	

==

# Choisir pltest ou soluce ou expectedoutput

pltest==
>>> distance1("xaxx","xbxx") # substitution 
2
>>> distance1("axxxa","xxx") # delete en premier en dernier
2
>>> distance1("xxx","axxxa") # insert en premier en dernier
2
>>> distance1("abaculexxxx","xxxxabacule")
8
==

