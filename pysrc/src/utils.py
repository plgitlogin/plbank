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
import sys
import re
import os



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


globaltaboo=False # par defaut pas de problem de taboo

# le checktaboo doit être fait en debut de grader
def checktaboo(taboo):
	"""
	check taboo est brutal
	il faudrais faire une analyse du code avec l'AST pour
	être sur que les mots clefs sont vraiment des mots clef
	pas des truc ou les loups 'bass' sont transformée en 'bbotom'.
	"""
	global globaltaboo
	globaltaboo = False 
	ltaboo = taboo.split('|')
	mots = open("student.py","r").read() #
	for x in ltaboo:
		reexp=re.compile(x)
		if reexp.search(mots) :
			globaltaboo = True
	return globaltaboo



def check_output(want, got):
	"""
	Return True iff the actual output from an example (`got`)
	matches the expected output (`want`).

	"""

	# If `want` contains hex-escaped character such as "\u1234",
	# then `want` is a string of six characters(e.g. [\,u,1,2,3,4]).
	# On the other hand, `got` could be another sequence of
	# characters such as [\u1234], so `want` and `got` should
	# be folded to hex-escaped ASCII string to compare.
	# FIXME i commanted out the 2 following lignes
	# FIXME should verify if bytes then decode(utf-8) 
	got = str(pldecode(got).encode('ASCII', 'backslashreplace'), "ASCII")
	want = str(pldecode(want).encode('ASCII', 'backslashreplace'), "ASCII")

	# Handle the common case first, for efficiency:
	# if they're string-identical, always return true.
	if got == want:
		return True

	# If a line in got contains only spaces, then remove the
	# spaces.
	got = re.sub('(?m)^\s*?$', '', got)
	if got == want:
		return True
	# This flag causes doctest to ignore any differences in the
	# contents of whitespace strings.  Note that this can be used
	# in conjunction with the ELLIPSIS flag.
	if True : # we want normelized white spaces
		got = ' '.join(got.split())
		want = ' '.join(want.split())
		if got == want:
			return True
	# We didn't find any match; return false.
	return False


def pldecode(s):
	if type(s) is str:
		return s
	else:
		return str(s.decode(encoding="utf-8", errors="strict"))

def dodump(dr,ev=0):
	#for key in ['execution','feedback','error','other','error']:
	#	dr[key]= '<br>'.join(dr[key].split("\n"))
	pld=getpldic()
	if "help" in pld:
		dr['feedback'] += pld["help"]
	if dr["success"] and "taboo" in pld and checktaboo(pld["taboo"]):
		print("taboo",file=sys.stderr)
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
	 "feedback": "# Erreur à l'exécution\n Il semble qu'une erreur de programmation c'est glissée dans votre code \n# la Sortie standard\n"+str(message),"errormessages" : "" , "other": "","error":"","execution":"" }
	dodump(dico_reponse)

def failure(message):
	"""
	Une erreur d'excution résultat non conforme aux attentes
	le message contient le nombre de tests réussis et le test en échec
	"""
	dico_reponse = { "success": False , "errormessages" : "" ,
	 "feedback": "#Mauvais résultat \n Il n'y a pas d'erreur dans votre code \n Mais il ne calcul pas le résultat attendu\n # Execution \n "+str(message), "other":"" ,"error":"","execution":""}
	dodump(dico_reponse)

def plateform(dexec,feedback="# Erreur Plateforme \n Un problème de la plateforme\\n parlez en au professeur\\n passez à l'exercice suivant"):
	feedback += "\n# Execution \n" + dexec['stdout']
	feedback += "\# Erreurs \n"+ dexec['stderr']+"\n"+error 
	dico_reponse = { "success": True , "errormessages" : "","feedback": feedback, "other": "","error":"","execution": ""
		}
	dodump(dico_reponse,ev=1)




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
		"procesus fils\\nj'ai lu  PAS DE PROBLEM DE LECTURE\\n"
		>>> d=exectojson("xx.py") # pas d'input
		>>> d['result']
		False
		>>> d['stdout']
		'procesus fils\\n'
		>>> exectojson(['-m','doctest','testofdoc.py'])
		>>> d['result']
		True

	"""
	# TODO can i check the existance of python3 ?
	# CHECKME no options
	if isinstance(target, str):
		args=['python3',target]
	elif isinstance(target, list):
		args=['python3']
		args.extend(target)
	else:
		raise TypeError(target)
	try:
		if infile:
			entry = open(infile, "rb")
			cp = subprocess.run(args, input=entry.read(),
				stdout=subprocess.PIPE,stderr=subprocess.PIPE,
				timeout=timeout)
		else:
			cp = subprocess.run(args, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,stderr=subprocess.PIPE, timeout=timeout)
		dico = {"plateforme":True,"stderr":cp.stderr.decode("utf-8"),"result":(cp.returncode==0),"stdout":cp.stdout.decode("utf-8"),"cp":cp,"pwd":os.getcwd()}
		return(dico)
	except (OSError, IOError) as e:
		dico = {"plateforme":False,"stderr":e,"result":False,"stdout":"PlateForme IO ERROR"}
	except subprocess.TimeoutExpired as toe:
		dico = {"plateforme":True,"stderr":toe,"result":False,"stdout":"temps d'execution trop long"}

	if jsonfile:
		with open(jsonfile,"w") as jsf:
			json.dump(dico, fp=jsf,sort_keys=True)
	return(dico)

def compiletest():
	"""
	>>> _createStudentCode("@ <- ça grosse erreur de compile ")
	>>> compiletest()
	Traceback (most recent call last):
	...
	SystemExit: 0
	>>> _createStudentCode("print('titi') ")
	>>> compiletest()
	True
	"""
	EEE=None
	import py_compile
	try:
		x= py_compile.compile("student.py",doraise=True)
	except Exception as EE:
		EEE=EE
	else:
		return True

	compileerror(str(EEE))








def createInputFile(pld,lastgenerated=True):
	# il faut pour tous les input* verifier que l'execution de student celle de soluce
    # ou bien faire inputgeneratorcalls appels à inputgenerator et verifier la même chose
	"""
	creates a file "input.txt" in current directory
	with the inputgenerator if it exist
	with the input field if it exist
	with input0 to input9 FIXME in this order
	the inputgenerator is considered random
		and new file will create each call

	>>> import os.path
	>>> if os.path.isfile("input.txt"): os.remove("input.txt")
	>>> plk={"inputgenerator":"import random\\nfor  n in range(10):\\n  print(random.randint(4,123))","input":None}
	>>> createInputFile(plk,lastgenerated=True)
	True
	>>> "inputgenerator" in plk
	False
	>>> os.path.isfile("input.txt")
	True
	>>> createInputFile({"inputgenerator":"import random\\nfor  n in range(10):\\n  print(random.randint(4,123))","input":"Toto"}) # ambiguité entre input et inputgenerator
	Traceback (most recent call last):
	...
	SystemExit: 0
	>>> if os.path.isfile("input.txt"): os.remove("input.txt")
	>>> createInputFile({"input": b"1\\n2\\n3\\n4\\n"})
	True
	>>> os.path.isfile("input.txt")
	True
	>>> createInputFile({"input4": b"5\\n5\\n5\\n5\\n"})
	True
	>>> createInputFile({})
	False
	"""

	if 'inputgenerator' in pld:
		with open("inputgen.py","w") as ig:
			print(pld["inputgenerator"],file=ig)
		d=exectojson("inputgen.py")
		if  'input' in pld and pld['input'] != None:
			# TODO remonter une erreur a l'auteur du test
			failure("INPUT ET INPUTGENERATOR AMBIGUITE\\n")
		pld['input']=d['stdout'] # on écrasse le input
		if lastgenerated:
			del pld['inputgenerator'] # doit repondre faux la prochaine fois
	elif not 'input' in pld:
		for i in range(0,10):
			s='input'+str(i)
			if s in pld:
				pld['input']=pld[s]
				del pld[s]
				break

	if 'input' in pld:
		with open("input.txt","w") as it :
			print(pldecode(pld['input']),file=it)
			del pld['input']
		return True
	else:
		return False # retourne faux si pas de input ou si fin des inputs prédéfinis


def compareexecution():
	"""
	check the execution of student with input = input.txt
	against the execution of soluce with input = input.txt
	"""
	dt= exectojson("soluce.py",infile="input.txt")
	ds= exectojson("student.py",infile="input.txt")
	if check_output(dt['stdout'],ds['stdout']):
		# TODO
		return True,"",""
	else:
		return False,str(dt['stdout']),str(ds['stdout'])

def dumpdic(dic):
	import json
	f=open("pl.json","w")
	print(json.dump(dic,f,sort_keys=True))
	f.close()
	return

def _createStudentCode(code):
	f=open("student.py","w")
	print(code,file=f)
	f.close()

def testexpectedoutput():
	pld=getpldic()
	if not createInputFile(pld): # il n'y a pas de fichier d'entrée
		d=exectojson("student.py")
	else:
		d=exectojson("student.py",infile="input.txt")
	if check_output(pld['expectedoutput'],d['stdout']):
		success(pld['expectedoutput'])
	else:
		message = "Votre script ne produit pas la bonne sortie.\n\nsortie attendue:\n" + pld['expectedoutput']
		message += "\n\nsortie optenue:\n\n" + pldecode( d['stdout'])
		erreurdexecution(message)


def testpltest():
	pld=getpldic()
	with open("pltest.py","w") as pltf :
		with open("student.py","r") as f:
			print("\"\"\"\n"+pld["pltest"]+"\"\"\"",file=pltf)
			print(f.read(),file=pltf)
	os.environ['TERM']="linux"# bug in readlinhttps://bugs.python.org/msg191824
	d=exectojson(['-m','doctest','pltest.py'])
	if d['result']:
		success("# Bravo \n\nTout les tests sont passés \n\n")
	else:
		erreurdexecution("\n\n".join(d['stdout'].split("\n"))


def testsoluce():
	pld=getpldic()
	if "generateinput" in pld:
		nbt2g = int(pld["generateinput"])
	NBT=0 # NOMBRE DE TESTS REUSSIT
	didcreate =  createInputFile(pld,lastgenerated=False)
	if not didcreate :
		plateform({}) # pas d'input définis ni de inputgenerator
	while  didcreate:
		r,want,got = compareexecution()
		if not r : # echec d'un test
			message= "# "+ str(NBT)+" tests réussits\n"
			message += "entree:\n"
			message += open("input.txt","r").read()
			message += "\nsortie attendue:\n" + str(want)
			message += "\nsortie optenue:\n" + str(got)
			failure(message)
		else:
			NBT+=1
			didcreate  =  createInputFile(pld, lastgenerated = (NBT<nbt2g) )
	message="%d tests passé avec succes " % NBT
	success(message)

def grade():
	"""
	# pour que ce test fonctionne il faut un fichier pl.json
	>>> dumpdic({"input":"1\\n2\\n","expectedoutput":"1\\n2\\n"})
	None
	>>> _createStudentCode("print(input())\\nprint(input())\\n")
	>>> d=grade()
	Traceback (most recent call last):
	...
	SystemExit: 0
	>>>
	"""
	
	pld=getpldic()
	if 'taboo' in pld:
		checktaboo(pld['taboo'])
	compiletest()
	if 'expectedoutput' in pld:
		return testexpectedoutput()
	elif 'pltest' in pld:
		return testpltest()
	elif 'soluce' in pld:
		return testsoluce()
	else:
		plateform(message="Utilisez une méthode d'évaluation expectedoutput,pltest,soluce\\n")


def main(args):
	print("ce fichier n'est pas un script principal",file=sys.stderr)
	return 1

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
