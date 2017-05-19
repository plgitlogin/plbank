# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Boites d'oeufs
title= Modulo et Diviser
tag= print|input|operator.mod|operator.floordiv
template=/python/IUT/template
text==

# Operator  // et % 

Joelle a des poules tout les matins elle ramasse les oeufs et les mets dans des boites.

Quand elle a fini de ramasser les oeufs elle appelle sont fils Emile en lui donnant le nombre d'oeufs pondus pendant la nuit, il doit calculer le nombre de boites de 6 oeufs et le nombre d'oeufs restants.

Aidons le avec // qui est la division entière et % (operateur modulo) qui calcul le reste de la division entiere. 

Remarque: Vieux sujet de CM2. 
==

files=@/pysrc/src/nomdefichierinexistant

code==
nbreoeufs = int( input("saississez le nombre d'oeufs :") )

print("Il faut "+ 333 + "boites.")
print("il restera "+ 222 + "oeufs.") 


==

grader==
print("bande de moules")
==

inputgenerator==
from random import randint

print(randint(10,100))
==

soluce==
nbreoeufs = int( input("saississez le nombre d'oeufs :") )

print("Il faut "+ nbroeufs // 6 + "boites.")
print("il restera "+ nbroeufs % 6 + "oeufs.") 

==

