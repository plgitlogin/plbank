#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  plutils.py
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


"""
Fonction utiles pour les grader PL.

"""
import json

dictrans={ "execution": "Exécution" ,"error":"Erreur","compile":"Compilation ","feedback":"Retours"}


def feedback(success=True,**kwargs):
	message=""
	d=  { "success": success , "execution" : "", "feedback": "", "other": "","error":""}
	for k in dictrans.keys():
		if k in kwargs.keys():
			message += "# "+dictrans[k] + "\n"
			message += kwargs[k] + "\n"
	d["feedback"]=message
	return json.dumps(d)


def dodump(dr,ev=0):
	#for key in ['execution','feedback','error','other','error']:
	#	dr[key]= '<br>'.join(dr[key].split("\n"))
	pld=getpldic()
	if "help" in pld:
		dr['feedback'] += pld["help"]
	if dr["success"] and "taboo" in pld and checktaboo(pld["taboo"]):
		dr["success"]=False
		dr['feedback'] += "# TABOOOOO \n\n Vous avez utilisé un terme interdit \n\n"+pld['taboo']
	print(json.dumps(dr))
	sys.exit(ev)


def success(message):
	dico_reponse = { "success": True ,
	"execution" : "",
	"feedback": "# Bravo ! \n\n vous avez réussit l'exercice\n"+message,
	"other": "","error":""}
	dodump(dico_reponse)


def compileerror(message):
	"""
	compileerror("les messages du compilateur pour l'execution ")
	
	"""
	message = "\n\n".join(pldecode(message).split("\n"))
	dico_reponse = { "success": False ,
	 "feedback": "# Erreur de compilation \n\n Le compilateur à détecté une erreur\n\n il faut la corriger\n\n"+message,"errormessages" : "" , "other": "","error":"","execution":"" }
	dodump(dico_reponse)

def erreurdexecution(message):
	"""
	appellez cette fonction quand il y a une exception dans l'execution
	i.e. stderr non vide
	appeller avec la concaténation de stdout et sdterr
	"""
	dico_reponse = { "success": False ,
	 "feedback": "# Erreur à l'exécution\n Il semble qu'une erreur de programmation\n s'est glissée dans votre code \n# la Sortie standard\n"+str(message),"errormessages" : "" , "other": "","error":"","execution":"" }
	dodump(dico_reponse)

def failure(message):
	"""
	Une erreur d'excution résultat non conforme aux attentes
	le message contient le nombre de tests réussis et le test en échec
	"""
	dico_reponse = { "success": False , "errormessages" : "" ,
	 "feedback": "#Mauvais résultat \n Il n'y a pas d'erreur dans votre code \n Mais il ne calcule pas le résultat attendu\n # Execution \n "+str(message), "other":"" ,"error":"","execution":""}
	dodump(dico_reponse)

def plateform(dexec,feedback="# Erreur Plateforme \n Un problème de la plateforme\\n parlez en au professeur\\n passez à l'exercice suivant"):
	feedback += "\n# Execution \n" + dexec['stdout']
	feedback += "\# Erreurs \n"+ dexec['stderr']+"\n"+error 
	dico_reponse = { "success": True , "errormessages" : "","feedback": feedback, "other": "","error":"","execution": ""
		}
	dodump(dico_reponse,ev=1)


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

