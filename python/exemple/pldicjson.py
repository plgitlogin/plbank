#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pldicjson.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  
#  Ce module fournis une fonction getpldic() qui lit le fichier pl.json du répertoire
# et retourne un dictionnaire de l'exercice 


import json


pldicsingleton=None

def getpldic():
	'''
	getpdic return the dictionnary contained in the file "./pl.json" 
	'''
	global pldicsingleton
	if pldicsingleton == None :
		try:
			pldicsingleton= json.load(open("pl.json","r"))
		except Exception as e:
			# TODO gestion des exceptions dans plExecutor
			pldicsingleton = dict() # retourne un dico vide 
	return pldicsingleton


