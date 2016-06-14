# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=Conversion des str et des int
tag=root # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate
text==

Le code suivant met en valeur la différence entre deux interprétation d'un mot écrit avec des chiffres.

==


inputgenerator==
print("1234")
==



code==
r = input()
print(r + r)
n = int(r)
print(n + n)
==

pltest==
>>> import json
>>> d = json.load(open("student.json","r"))
>>> not "12341234\n2468\n" !=  d["stdout"]
True
>>>
==

