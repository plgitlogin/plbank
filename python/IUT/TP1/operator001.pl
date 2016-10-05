# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Boites d'oeufs
title= Modulo et Diviser
tag= print|input|operator.mod|operator.floordiv
template=/python/IUT/template
text==

# Operator  // et % 

Joelle a des poules tout les matins elle ramasse les oeufs et les mets dans des boites.

Quand elle a fini de ramasser les oeufs elle appelle sont fils en lui donnant le nombre d'oeuf, il doit calculer le nombre de boites de 6 oeufs et le nombre d'oeufs restants.

Aidons le avec // qui est la division entière et % (opérateur modulo) qui calcul le reste de la division entière. 




==

code==
nbreoeufs = int( input("saisissez le nombre d'oeufs :") )

b=  # votre opération 
r=  # votre opération

print("Il faut "+ b + "boites.")
print("il restera "+ r + "oeufs.") 


==

inputgenerator==
from random import randint

print(randint(10,100))
==

soluce==
nbroeufs = int( input("saisissez le nombre d'oeufs :") )

print("Il faut "+ nbroeufs // 6 + "boites.")
print("il restera "+ nbroeufs % 6 + "oeufs.") 

==

