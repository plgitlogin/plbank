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
>>> d = json.load("student.json")
>>> d["stdout"]=="bob"
True
>>>
==
