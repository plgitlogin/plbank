#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  utils.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  
# help functions to use in the PL project 
# 
#

import subprocess
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
			pldicsingleton = {"plateforme":False,
				"stderr":e,"result":False,
				"stdout":"PlateForme IO ERROR"}
	return pldicsingleton



def exectojson(target,infile=None,jsonfile=None,timeout=1):
	"""
	exectojson execute the shell process
	python3 target <infile
	catches the result, stdout, stderr of this process and
	return a dictionnary with these three values
	if jsonfile != None:
		a jsondump of the dictionnary is done in the file named jsonfile
	the process is kill after a timeout (1 default) seconds 


		>>> d=exectojson("xx.py",infile="entrrrrrrree.tex")
		>>> d['result']==False
		True
		>>> d['stdout'] == "PlateForme IO ERROR"
		True

		>>> f=open("entree.tex","r")
		>>> d=exectojson("tolong.py",infile="entree.tex")
		>>> d['result']
		False
		>>> d['stdout']
		"temps d'execution trop long"

		>>> d=exectojson("xx.py",infile="entree.tex")
		>>> d['result']
		True
		>>> d['stdout']
		b"procesus fils\\nj'ai lu  PAS DE PROBLEM DE LECTURE\\n"
		>>> d=exectojson("xx.py") # pas d'input 
		>>> d['result']
		False
		>>> d['stdout']
		b'procesus fils\\n'


	"""
	# TODO can i check the existance of python3 ?
	# CHECKME no options
	args=['python3',target]
	try:
		if infile:
			entry = open(infile, "rb")
			cp = subprocess.run(args, input=entry.read(),
				stdout=subprocess.PIPE,stderr=subprocess.PIPE,
				timeout=timeout)
		else:
			cp = subprocess.run(args,
				stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
				stderr=subprocess.PIPE, timeout=timeout)
		dico = {"plateforme":True,"stderr":cp.stderr,"result":cp.returncode==0,"stdout":cp.stdout}
	except (OSError, IOError) as e:
		dico = {"plateforme":False,"stderr":e,"result":False,"stdout":"PlateForme IO ERROR"}
	except subprocess.TimeoutExpired as toe:
		dico = {"plateforme":True,"stderr":toe,"result":False,"stdout":"temps d'execution trop long"}

	if jsonfile:
		with open(jsonfile,"w") as jsf:
			json.dump(dico, fp=jsf)
	return(dico)



def execstudent(inputfile="input",jsonfile=None):
	dico= exectojson("student.py")

def createInputFile(pld):
	"""
	creates a file "input.txt" in current directory
	with the inputgenerator is it exist
	with the input field if it exist
	the inputgenerator is considered random
		and new file will create each call

	>>> import os.path
	>>> os.remove("input.txt")
	>>> createInputFile({"inputgenerator":"import random\\nfor  n in range(10):\\n  print(random.randint(4,123))","input":None})
	True
	>>> os.path.isfile("input.txt")
	True
	""" 
	if pld["inputgenerator"]:
		with open("inputgen.py","w") as ig:
			print(pld["inputgenerator"],file=ig)
		d=exectojson("inputgen.py")
		if pld['input']:
			# TODO remonter une erreur a l'auteur du test 
			failure(d,error="INPUT ET INPUTGENERATOR AMBIGUITE\\n")
		pld['input']=d['stdout'] # on écrasse le input 
	if pld['input']:
		with open("input.txt","w") as it :
			print(pld['input'].decode(encoding="utf-8", errors="strict"),file=it)
		return True



def grade():
	pld=getpldic()
	if pld['expectedoutput']:
		if not createInputFile(pld): # il n'y a pas de fichier d'entrée 
			d=execstudent()
		else:
			d=execstudent(inputfile="input.txt")
		if pld['expectedoutput']==d['stdout']:
			success(d)
		else:
			failure(d,message="Votre script ne produit pas la bonne sortie\\n")
	elif pld['pltest']:
		failure(d,error="pas IMPLEMENTE ENCORE \\n")
	elif pld['soluce']:
		failure(d,error="pas IMPLEMENTE ENCORE \\n")
	else:
		failure(d,error="Utilisez une méthode d'évaluation expectedoutput,pltest,soluce\\n")


def main(args):
	print("ce fichier n'est pas un script principal",file=sys.stderr)
	return 1

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
