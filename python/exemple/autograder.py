#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  autograder.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



import sys
import json 
import pldoctest
import io

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
		if dicjson["feedback"]:
			dico_reponse["feedback"] = dicjson["feedback"]
		else:
			dico_reponse["feedback"] = ""
	dico_reponse["other"]=other
	print(json.dumps(dico_reponse)) 

def doBad(success=False,error="Des erreurs dans l'exécution",execution="pas de sorties",feedback="Corrigez votre code",other=""):
	dico_reponse["success"]=success
	dico_reponse["error"]=error
	dico_reponse["execution"]="<br>".join(execution.split("\n"))
	dicjson = getpldic()
	if dicjson["feedbackfalse"] :
		dico_reponse["feedback"] = dicjson["feedbackfalse"]
	else:
		dico_reponse["feedback"]=feedback
	dico_reponse["other"]=other
	print(json.dumps(dico_reponse)) 


def compiletest():
	import py_compile
	with io.StringIO() as errors:
		oldstderr=sys.stderr
		sys.stderr=errors
		try:
			x= py_compile.compile("student.py",doraise=True)
		except py_compile.PyCompileError as EEE:
			err = str(sys.stderr.getvalue())
			sys.stderr= oldstderr
			
			doBad(error="Erreur de compilation de votre code<br>", errormessages = str(EEE), execution=err)
			return False
	return True



def grade(o):
	if compiletest() :
		with io.StringIO() as bob:
			# TODO il faut tester si le code compile avant de lancer les test pour clarifier les messages d'erreurs 
			oldstd = sys.stdout
			sys.stdout = bob
			failures,tests = pldoctest.pltestfile(o,name=" Votre Code <br> ",optionflags=pldoctest.REPORT_ONLY_FIRST_FAILURE)
			sys.stdout=oldstd
			if failures ==0:
				doGood(execution=bob.getvalue())
			else:
				doBad(execution=bob.getvalue(),feedback=" %d tests raté sur %d " % (failures,tests))


def autograde():
	dicjson = getpldic()
	grade(dicjson["pltest"])


if __name__ == '__main__':
	dicjson = getpldic()
	grade(dicjson["pltest"])


