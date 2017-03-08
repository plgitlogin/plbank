# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=testok.pl
title=   # N'oubliez pas de remplir ce champs svp
tag=  # N'oubliez pas de remplir ce champs svp
template=/python/test/template.pl

text==


==

grader==


>>> try:
		import utils
	except ImportError as ie:
		dico = {"plateforme":True,"stderr":toe,"result":False,"stdout":"temps d'execution trop long"}
		"Problème le fichier ",ie.name,"est abscent de l'environnement d'execution")
		
>>>  try:
		import plutils
	except ImportError as ie:
		print("Problème le fichier ",ie.name,"est abscent de l'environnement d'execution")
>>>  try:
		import pldoctest
	except ImportError as ie:
		print("Problème le fichier ",ie.name,"est abscent de l'environnement d'execution")

==
