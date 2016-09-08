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
import pldicjson 

__pl__="""
	Utilise la balise pltest comme élément de test 
	"""


dico_reponse = { "success": True , "errormessages" : "" , "execution": "Error", "feedback": "", "other": "" }

from pldicjson import getpldic,getstudic,getsoldic


def doGood(success=True,error="",execution="OK",feedback=None,other=None):
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
	if other :
		dico_reponse["other"]=other
	print(json.dumps(dico_reponse))
	sys.exit()

def doBad(success=False,error="Des erreurs dans l'exécution",execution="pas de sorties",feedback="Corrigez votre code",errormessages="",other=None):
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
	if other :
		dico_reponse["other"]=other
	print(json.dumps(dico_reponse))
	sys.exit()

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
	stu = getstudic()
	if "stderr" in stu and stu["stderr"] != "":
		doBad(execution="Erreur d'execution de votre code<br>", errormessages = stud["stderr"])
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
	sys.exit()

def testoutput():
	"""TODO
	modifier pour accepter input0-NUM correspondant à expectedoutput0-NUM
	les feedback0-NUM si il existe sont associés en cas d'erreur 
	"""
	dicjson = getpldic()
	if not "expectedoutput" in dicjson :
		doBad(execution=" Corriger votre sujet balise 'expectedouput' manquante")
		sys.exit()
	value = dicjson["expectedoutput"]
	import json
	d = getstudic()
	if d["stderr"] != "":
		doBad(error="Erreur d'execution de votre code<br>")
	if not "stdout" in d:
		return False
	if  value ==  d["stdout"]:
		doGood(execution=value)
	if  "".join(d["stdout"].split()) ==  "".join(value.split()):
		doGood(other=d["stdout"],feedback="C'est juste aux caractères d'espacement près")
	else:
		doBad(execution= d["stdout"],other="Attendu: "+value+"\nobtenu:"+d["stdout"])

def testsoluce():
	"""
	TODO modifier pour accepter un certain nombre d' input0-Num qui permettent de tester
	les feedback0-Num peuvent êre associers  
	"""
	sol = getsoldic()
	stu = getstudic()
	if stu["stderr"] != "":
		doBad(execution="Erreur d'execution de votre code<br>")
	if not "stdout" in stu:
		doBad(execution="Attendu: "+sol["stdout"]+"\nobtenu: rien ")
	if sol["stdout"] == stu["stdout"] and stu["stderr"]== "":
		doGood(execution=stu["stdout"])
	if  "".join(sol["stdout"].split()) ==  "".join(stu["stdout"].split()):
		doGood(execution=stu["stdout"],feedback="C'est juste aux caractères d'espacement près")
	else:
		doBad(execution="Attendu: "+sol["stdout"]+"\nobtenu:"+stu["stdout"])




def autograde():
	dicjson = getpldic()
	if "pltest" in dicjson :
		grade(">>> from student import * \n"+dicjson["pltest"])
	if "expectedoutput" in dicjson :
		testoutput()
	if "soluce" in dicjson:
		testsoluce()

if __name__ == '__main__':
	compiletest()
	autograde()



