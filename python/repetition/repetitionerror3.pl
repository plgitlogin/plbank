# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=repetitionerror3.pl
title= Correction d'erreurs 
tog=error
template=/python/exemple/autogradertemplate

# n'oubliez pas d'indenter votre code dans le texte de l'exercice pour que cela soit interprété comme du code.
text==

Un exercice de correction d'erreurs de syntaxe.


Corriger le code suivant :
	# le code de la table de multiplication par 6  
	for y in range(0,10)
		print("y * 6 = , Y * 6 )

Une fois corrigé il doit afficher:
	0 * 6 = 0
	1 * 6 = 6
	etc.


==
feedback==
Beaucoups d'erreurs ? parfois il faut mieux jeter le code et le reprendre au début.<br>

	On lit plusieurs fois le code que l'on écrit : soyez gentil avec vous même écrivez du code lisible ...

==

# n'oublier pas de la copier dans l'éditeur
code==
	# le code de la table de multiplication par 6  
	for y in range(0,10)
		print("y * 6 = , Y * 6 )
==



# Choisir expectedoutput
# exéctuter le code corrigé et copiez la sortie standard dans cette balise
expectedoutput==
0 * 6 = 0
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
4 * 6 = 24
5 * 6 = 30
6 * 6 = 36
7 * 6 = 42
8 * 6 = 48
9 * 6 = 54
==
