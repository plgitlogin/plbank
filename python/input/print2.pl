# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=Utilisation de print
title=La fonction print
tag=print
template=/python/exemple/autogradertemplate
text==

Utilisons la fonction **print** pour faire un affichage.
tester l'affichage deu code suivant:

	print("+" * 3)

en déduire l'affichage de l'image suivante
+
++
+++
++++
+++++

==

code==
print("+"*3)
==

expectedoutput==
+
++
+++
++++
+++++
==

feedback==
Très bien a chaque fois que vous souhaitez avoir une information pendant l'execution de votre programme il suffit de faire un **print** de 
cette information.<br>
Remarque en python 2 les paranthèses ne sont pas nécessaire, mais garder l'habitude de les utiliser.
==
