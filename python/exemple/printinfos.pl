# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=printinfos.pl
tag=root # N'oubliez pas de remplir ce champs svp
template=/python/function/functiongradertemplate
text==

Clicker sur check 

==

grader==

import sys
import json
dico_good = { "success": True , "errormessages" : "" , "execution": "OK", "feedback": "ok", "other": "" }
dico_bad = { "success": False , "errormessages" : "création d'une exception", "execution": "", "feedback": "modifier votre valeur", "other": "" }

def doGood(success=True,error="",execution="OK",feedback="Bravo",other="tutututu"):
	dico_good["success"]=success
	dico_good["error"]=error
	dico_good["execution"]=execution
	dico_good["feedback"]=feedback
	dico_good["other"]=other
	print(json.dumps(dico_good)) 

import os

x = json.load(open("student.json","r"))
f = x["stdout"]
doGood(execution=(sys.version+str(sys.path)),feedback=str(os.listdir("/var/lib/upem/)),other=f,error=str(x))

==

inputgenerator==
print(12)
==

comment==
if soluce ['soluce.py', 'grader.py', 'student.py', 'pl.json', 'pldicjson.py', 'functiongrader.py', 'student.json', 'pldoctest.py', 'soluce.json', 'environment']
with out soluce :
		['grader.py', 'student.py', 'pl.json', 'pldicjson.py', 'functiongrader.py', 'student.json', 'pldoctest.py', 'environment']

==

Xsoluce==
# une solution de l'exercice
# utile pour les tests



==
