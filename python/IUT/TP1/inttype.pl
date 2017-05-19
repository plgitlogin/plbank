# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz
name=Des Entiers
title= Des entiers
tag= int|str|type|litteral|variable

# je ne suis pas sur d'avoir besoin de ca FIXME 
#template=/python/0PLG/template


text==


# Des entiers

Réalisons quelque calcul avec des entiers.

Utilisez l'interpréteur


==
code==
# Ceci est un commentaire
# creez vos trois variables sur les lignes suivantes
# une variable par ligne

==

gradertype=autonome

grader==

import json
import sys
d=  { "success": False , "execution" : "", "feedback": "", "other": "","error":""}


try:
	from  student import entier,bob,nom
	entier>0
	bob>0
	nom=="Emilie"
except NameError as ne:
	d["feedback"]="# oubli\n\n Vous n'avez pas définie la variable **" +  str(ne).split("'")[1]+"**\n"
	print(json.dumps(d))
	sys.exit(1)
except ImportError as ie:
	d["feedback"]="# oubli\n\n Vous n'avez pas définie la variable **" +  str(ie).split("'")[1]+"**\n"
	print(json.dumps(d))
	sys.exit(1)
except Exception as e:
	d["feedback"]="# Problem dans le code\n\n"+str(e)
	print(json.dumps(d))
	sys.exit(1)
if not type(entier) == type(3):
	d["feedback"]="# Type incorrect\n\nla variable entier n'est pas entière \n type(entier) =: " +str(type(entier))  
elif not type(bob) == type(3.12):
	d["feedback"]="# Type incorrect\n\nla variable bob n'est pas un float (réel) \n type(bob) =: " +str(type(bob))  
elif not type(nom) == type(" toto "):
	d["feedback"]="# Type incorrect\n\nla variable nom n'est pas une chaine \n type(nom) =: " +str(type(nom))
else:
	d=  { "success": True , "execution" : "",
	 "feedback": "#bravo \n\nTrois variables que nous allons utiliser dans un programme ;)\n", "other": "","error":""}

print(json.dumps(d))


==

testcode==
entier=123
bob=5.5
nom="jkh"
==

