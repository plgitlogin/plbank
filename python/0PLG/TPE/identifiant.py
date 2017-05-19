#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  identifiant.py
#  
#  Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>


import re

ident = re.compile("^[_a-zA-Z][_0-9a-zA-Z]*$")

tableau=[
	(["1a","42","0612567"],
	"Désolé mais **%s** n'est pas un identifiant correct.\nIl peut être confondu avec un entier.\n Aucun identifiant ne peut commencer par un chiffre.\n Par contre a1 est correct.\n Posez vous la question que ce passe t'il s'il l'on change le sens d'un nombre?\n Si 3 devient assiette ... \n "),
	(["b*3","carre[2]","truc()"],
	" **%s** est le résultat d'une opération du langage c'est donc une expression ou une instruction, mais pas un identifiant.\n le caractère * est la multiplication.\n Les crochets [] permettent de manipuler les indices. \n les parenthèse sont liés aux fonctions.\n"),
	(["@a","?uu","€3","£5"],
	(" les caractère non-alphabétiques ne sont pas autorisés dans les identificateurs.\n %s n'est donc pas un identificateur.\n"),
	(["and","as","assert","break","class","continue","def","del","elif","else","except","exec","finally","for","from","global","if","import","in","is","is not","lambda","not","or","pass","print","raise","return","sort","try","while","yield"],
                " **%s est un mot réservé du langage. C'est un mot réservé qui a un sens précis pour le langage et n'est donc pas utilisable pour une variable, car cela créerai une ambiguité.\n"),
	(["Je ne suis pas un identifiant"],
	"le caractère espace permet de séparer/découper les mots et donc les identificateurs, il n'est donc pas autorisé dans un identificateur.\n **%s** n'est donc pas un identificateur."),

	(["42"], "**%s** est un entier et donc pour ne pas avoir d\'ambiguïté entre des valeurs entière et des identificateurs les valeurs entières ne sont pas des identificateurs.")
]
