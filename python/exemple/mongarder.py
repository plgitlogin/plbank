

import sys
import json 
import io

dico_good = { "success": True , "errormessages" : "" , "execution": "OK", "feedback": "ok", "other": "" }
dico_bad = { "success": False , "errormessages" : "création d'une exception", "execution": "", "feedback": "modifier votre valeur", "other": "" }



try:
	bob = io.StringIO()
	oldstd = sys.stdout
	sys.stdout = bob
	import student
	dico_good["execution"]= bob.getvalue()
	print(json.dumps(dico_good),file=oldstd)
except Exception as e:
	print(e)
	print(json.dumps(dico_bad))
