#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  taboo.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  
#  This program define the testtaboo() function that return a dict of the pl file in argument
# 



from pldicjson import getpldic



def testtaboo():
	'''
	test if the code in student.py contains a word in the taboo primitive of the pl.json file
	return "Le Taboo n'est pas respecté" if the word is present
	return None if it's is not present
	'''
	dic = getpldic()
	if dic["taboo"]:
		codestudent=""
		with open("student.py","r") as sf:
			codestudent = "".join( sf.readlines() )
		for w in dic["taboo"].split('|'):
			if w in codestudent:
				return "Le Taboo n'est pas respecté"
	return None
