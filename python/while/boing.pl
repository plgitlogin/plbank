# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=Boing 
title= Boing  # N'oubliez pas de remplir ce champs svp
tag=while|boucle|exposant  # N'oubliez pas de remplir ce champs svp
template=/python/0PLG/template.pl
text==

# Boing

Une balle tombe d'une certaine hauteur fournie par l'utilisateur.
A chaque rebond la hauteur diminue de 10% arrondi à l'entier le plus proche avec la fonction Mathématique .
Votre programme doit afficher les hauteurs successives tant qu'elles sont supérieur à 5.


Si la hauteur de départ est inférieur à 5 rien ne s'affiche !


==

code==
# Hauteur de la balle
h=int(input())
# boucle

print(round(h))

==
soluce==
h=int(input())
while h > 5 :
	h=h*0.9
	print(round(h))
==



