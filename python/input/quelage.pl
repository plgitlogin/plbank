# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title= Quel age à le capitaine
tag=input|print|variable
template=/python/0PLG/template.pl
name=Capitaine
text==
Demandez au Capitaine son année de naissance puis calculez et affichez son age au 31 décembre 2018 à Minuit.

  Le capitaine auras XXX ans en 2018.
== 

code==
# 
annee=int(input())
# Le capitaine auras XXX ans.

==

feedback==
Ok top passons à quelque chose de plus dur ;). 
==

inputgenerator==
from random import randint 
print(randint(10,78)+1939)

==

soluce==
a=int(input())
print("Le capitaine auras %d ans en 2018." % (2018-a))
==
