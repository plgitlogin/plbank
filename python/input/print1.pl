# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=print1.pl
title=La fonction print
tag=print
template=/python/exemple/autogradertemplate
text==

La fonction **print** permet de faire des affichages (envois de caractère à l'écran).

Nous allons l'utiliser pour écrire votre premier programme python.

Ecrivez une ligne de code de la forme :


print("votreprénomentreguillemets")

==

code==
print($$$$$$$$$$)
==

# Choisir pltest ou soluce ou expectedoutput

pltest==
>>> print("ok")
ok
==
feedbackfalse==
L'appel de la fonction print doit être fait avec une chaine c'est à dire des caractères entre deux guillemets.
==

feedback==
Très bien a chaque fois que vous souhaitez avoir une information pendant l'execution de votre programme il suffit de faire un **print** de 
cette information.<br>
Remarque en python 2 les parenthèses ne sont pas nécessaire, mais garder l'habitude de les utiliser.
==