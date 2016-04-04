
# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=tuple_template.pl
text==

==

code==
# Veuillez saisir votre code ici

==
grader==
import sys
import json 


dico_good = { "success": True , "errormessages" : "" , "execution": "OK", "feedback": "ok", "other": "" }
dico_bad = { "success": False , "errormessages" : "création d'une exception", "execution": "", "feedback": "modifier votre valeur", "other": "" }


try:
	import student
	print(json.dumps(dico_good))
except:
    print(json.dumps(dico_bad))
==

