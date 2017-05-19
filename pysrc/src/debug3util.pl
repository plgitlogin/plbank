# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Debuger  pltest avec check.py 
title= pas important 
tag=olebotag
template=/python/IUT/template.pl
text==

ecrire une fonction tyty qui retourne sont parametre multiplier par 3.

cet exercice est utilisé pour tester si check.py fonctionne

python3 check.py /pysrc/src/debug3util.pl devrait afficher un text du genre :


	test compil ok
    test correct ok
    
 Fin du Test 



==

code==
def tyty(t):
	return 3*t
==

pltest==
# toujours bon pas de test dans le pltest
==



testcode==
def tyty(y):
	return y*3
==
