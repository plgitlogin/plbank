# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title= Egal = Egal ? 
tag=input|print|variable
template=/python/exemple/autogradertemplate

text==
Ecriver un programme utilisant une unique variable **age** qui affiche
'''
Le capitaine à X ans. Dans deux ans il auras XX ans.
'''
puis Sachant que dans cinq ans, le perroquet aura le tiers de l’âge du capitaine (arrondi à l'année inférieur) 
'''
Le perroquet du capitaine à XXX ans.
'''

== 

code==
# 
age=int(input())
# Le capitaine à X ans. Dans deux ans il auras XX ans.
# Le perroquet du capitaine à XXX ans.
==

feedback==
Les opérateur de python permettent d'écrire des expressions complexe et rapide il n'est pas nécessaire de avoir un nom pour toutes les valeurs intermédiaires. 
==

inputgenerator==
from random import randint 
print(randint(10,40)+10))

==

soluce==
a=int(input())
print("Le capitaine à %d ans. Dans deux ans il auras %d ans." % (a,a+2))
print("Le perroquet du capitaine a %d " % ((a+5)/3))
==
