import sys
import json 
import random
import io

dico_good = { "success": True , "errormessages" : "" , "execution": "OK", "feedback": "ok", "other": "" }
dico_bad = { "success": False , "errormessages" : "création d'une exception", "execution": "", "feedback": "modifier votre valeur", "other": "" }



try:
	bob = io.StringIO()
	oldstd = sys.stdout
	sys.stdout = bob
	import student
	a=random.randint(1,20)
	b=random.randint(1,20)
	
	if binop(a,b) == a*b :
		dico_good["execution"]= "la fonction binop(%s , %s ) retourne  un résultat exacte %s " % (a,b,binop(a,b))
		print(json.dumps(dico_good),file=oldstd) 
	else:
		dico_bad["execution"] = "la fonction binop(%s , %s ) retourne  un résultat erroné %s alors que le résultat attendu est %s" % (a,b,binop(a,b),a*b) 
		print(json.dumps(dico_bad),file=oldstd)
except Exception as e:
	dico_bad["errormessages"]= str(e)
	print(json.dumps(dico_bad),file=oldstd)

