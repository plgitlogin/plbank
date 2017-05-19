# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Debuger  pltest avec check.py 
title= pas important 
tag=olebotag
template=/python/exemple/autogradertemplate.pl
text==

ecrire une fonction tyty qui retourne sont parametre multiplier par 3.

cet exercice est utilisé pour tester si check.py fonctionne

python3 check.py /pysrc/src/debug2.pl derai afficher un text du genre :

	test compil ok
 votre correction ne fonctionne pas :  b'{"feedback": " 1 tests rat\\u00e9 sur 4 ", "execution": "-+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+-<br>Failed example:<br>    tyty(0)<br>Attendu:    CECI EST UN MAUVAIS RESULTAT ATTENDU<br> obtenu:     0<br>-+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+--+-*-+-<br>1  jeu de tests avec des probl\\u00e8mes :<br>   1 tests sur   4 dans  Votre Code <br> <br>***Tests \\u00e9chou\\u00e9s*** 1  erreurs.<br>", "success": false, "errormessages": "", "other": null, "error": "Des erreurs dans l\'ex\\u00e9cution"}\n'
 Fin du Test 



==

code==
def tyty(t):
	return 3*t
==

pltest==
>>> tyty(15)
45
>>> tyty(3)
9
>>> tyty(0)
CECI EST UN MAUVAIS RESULTAT ATTENDU
==



testcode==
def tyty(y):
	return y*3
==

