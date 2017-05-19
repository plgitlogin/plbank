# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=repetitionerror2.pl
title= Correction d'Erreurs 
tog=error
template=/python/exemple/autogradertemplate

# n'oubliez pas d'indenter votre code dans le texte de l'exercice pour que cela soit interprété comme du code.
text==

Un exercice de correction d'Erreur de syntaxe.


Corriger le code suivant :
	# le code 
	for i in range(6):
	print(i)
	print("Hop")

Il doit afficher les entiers 0 à 5 (bornes comprises) chacun sur une ligne puis Hop.

==
feedback==
Un grand classique oublier l'indentation qui permet de spécifier ce qui fait partie de la boucle et ce qui est après.
Attention parfois il n'y pas d'erreur de syntaxe mais une erreur de code qui fait que votre code ne fait pas ce que vous souhaitez.
==

# n'oublier pas de la copier dans l'éditeur
code==
# le code
for i in range(6):
print(i)
print("Hop")



==



# Choisir expectedoutput
# exéctuter le code corrigé et copiez la sortie standard dans cette balise
expectedoutput==
0
1
2
3
4
5
Hop
==
