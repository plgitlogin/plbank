import sys
import json 
import random
import io

dico_good = { "success": True , "errormessages" : "" , "execution": "OK", "feedback": "ok", "other": "" }
dico_bad = { "success": False , "errormessages" : "création d'une exception", "execution": "", "feedback": "modifier votre valeur", "other": "" }

student=None
def hiddenimport():
	global student
	'''
	réalise l'import de student
	si il y a un problème d'execution termine l'execution du grader avec les informations de l'exception.
	redirection de la sortie standard dans un StringIO pour ne pas polluter la sortie standard.
	'''
	try:
		bob = io.StringIO()
		oldstd = sys.stdout
		sys.stdout = bob
		import student
		sys.stdout=oldstd
	except Exception as e:
		sys.stdout=oldstd
		dico_bad["errormessages"]= str(e)
		dico_bad["execution"]= bob.getValue()
		print(json.dumps(dico_bad))


hiddenimport()

# le code haut dessus de cette ligne ne seras plus visible dans la prochaine version

a=random.randint(1,20)
b=random.randint(1,20)


if student.binop(a,b) == a*b :
	dico_good["execution"]= "la fonction binop(%s , %s ) retourne  un résultat exacte %s " % (a,b,student.binop(a,b))
	print(json.dumps(dico_good)) 
else:
	dico_bad["execution"] = "la fonction binop(%s , %s ) retourne  un résultat erroné %s alors que le résultat attendu est %s" % (a,b,binop(a,b),a*b) 
	print(json.dumps(dico_bad))

