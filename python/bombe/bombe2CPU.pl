# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= bombe2CPU.pl
title=  bombe2CPU.pl
text==

bombe2CPU



==

# Choisir pltest ou soluce ou expectedoutput


grader==

import randint
import json

l=[0]
for i in range(1,2**30):
	l.append(randint(1,10000))

json.dumps({"plateforme":True,"stderr":"","result":True,"stdout":"temps d'execution trop long"})
==
