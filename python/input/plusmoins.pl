# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=Manipulation de Nombre
tag=root # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate

text==
Ecrire un programme qui demande à l’utilisateur de saisir quatre entiers au clavier (un par ligne), affiche ensuite une valeur par ligne, puis leur somme et leur moyenne sur la ligne suivante. Par exemple, si l’utilisateur entre les valeurs 12, 3, 14 et 5, le programme affiche :
12
3
14
5
somme= 34 , moyenne = 8.5
== 

feedback==

Deux solutions :<br>
	print("somme = ",somme," , moyenne = " ,moyenne)<br>
ou la syntaxe avec % mais attention c'est un float<br>
	print("somme = %d , moyenne = %.1f" % (somme,moyenne))
==

inputgenerator==
print(12)
print(3)
print(14)
print(5)
==

soluce==
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(a)
print(b)
print(c)
print(d)
s=a+b+c+d
print("somme = %d , moyenne = %.1f" % (s,s/4) )
==
