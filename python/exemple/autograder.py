#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  autograder.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  



import sys
import json 
import pldoctest
import io
from pldicjson import getpldic

__pl__="""
	Utilise la balise pltest comme élément de test 
	"""


dico_reponse = { "success": True , "errormessages" : "" , "execution": "Plateforme Error", "feedback": "", "other": "" }

from pldicjson import getpldic


def doGood(success=True,error="",execution="OK",feedback=None,other=""):
	dico_reponse["success"]=success
	dico_reponse["error"]=error
	dico_reponse["execution"]=execution
	if feedback != None:
		dico_reponse["feedback"]=feedback
	else:
		dicjson = getpldic()
		if "feedback" in dicjson:
			dico_reponse["feedback"] = dicjson["feedback"]
		else:
			dico_reponse["feedback"] = ""
	dico_reponse["other"]=other
	print(json.dumps(dico_reponse)) 

def doBad(success=False,error="Des erreurs dans l'exécution",execution="pas de sorties",feedback="Corrigez votre code",errormessages="",other=""):
	dico_reponse["success"]=success
	dico_reponse["error"]=error
	dico_reponse["execution"]="<br>".join(execution.split("\n"))
	dicjson = getpldic()
	if "feedbackfalse" in dicjson :
		dico_reponse["feedback"] = dicjson["feedbackfalse"]
	else:
		dico_reponse["feedback"]=feedback
	dico_reponse["other"]=other
	dico_reponse["errormessages"] = errormessages
	print(json.dumps(dico_reponse)) 

def __gg__(l):
	for u in l:
			yield str(u)


import builtins
def mockinput(thelist):
	bob = __gg__(thelist)
	builtins.input = lambda prompt="toto":  str(next(bob))

from importlib import import_module, reload 
student=None

def doloadstudent():
	global student
	if student == None:
		student = import_module("student")
	else:
		reload(student)


def dostudent(l):
		mockinput(l)
		doloadstudent()







def compiletest():
	import py_compile
	try:
		x= py_compile.compile("student.py",doraise=True)
	except py_compile.PyCompileError as EEE:
		doBad(error="Erreur de compilation de votre code<br>", errormessages = str(EEE))
		return False
	return True



def grade(o):
	if compiletest() :
		with io.StringIO() as bob:
			oldstd = sys.stdout
			sys.stdout = bob
			failures,tests = pldoctest.pltestfile(o,name=" Votre Code <br> ",optionflags=pldoctest.REPORT_ONLY_FIRST_FAILURE)
			sys.stdout=oldstd
			if failures ==0:
				doGood(execution=bob.getvalue())
			else:
				doBad(execution=bob.getvalue(),feedback=" %d tests raté sur %d " % (failures,tests))
		sys.exit()
	doGood(execution="problème avec la plateforme")

def autograde():
	dicjson = getpldic()
	grade(dicjson["pltest"])

def testoutput():
	dicjson = getpldic()
	if not "expectedoutput" in dicjson:
		doBad(execution=" Corriger votre sujet d'exercice la balise ‘expectedouput‘ est manquante")
		sys.exit()
	value = dicjson["expectedoutput"]
	import json
	d = json.load(open("student.json","r"))
	if not "stdout" in d:
		return False
	if  value ==  d["stdout"]:
		doGood(execution=value)
	else:
		doBad()


if __name__ == '__main__':
	dicjson = getpldic()
	grade(dicjson["pltest"])


