# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=recurrence1.pl
title=   Un premier exemple de programmation d'une Récurrence
tog=recursive
template=/python/exemple/autogradertemplate
text==

Caluler une formule de récurrence l'exemple le plus classique est la suite de Fibonacci (https://fr.wikipedia.org/wiki/Suite_de_Fibonacci).

Combien de lapin au bout de n mois.
Le premier mois un couple de lapin.
Le deuxième mois un couple de lapin et un couple de lapins immatures.
Le troisième moi deux couples de lapins et un couple de lapins immatures.

La remarque formule de récurrence dit un N ième mois il y auras les couples de lapins du mois dernier plus les descendant matures des couples du mois d'avant soit :

TODO latex ceci
	fibo(0)= 1  premier mois
	fibo(1)= 1  deuxième mois
	fibo(mois) = fibo(mois-1) + fibo(mois-2)

La 


# récurrences pas simple akerman
# f(n)= f(n-1)+ f(n//f(n-1))  f(1)=1 f(0)=0 


==

# Choisir pltest ou soluce ou expectedoutput

