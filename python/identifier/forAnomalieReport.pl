# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=correctidentifiers.pl
tag=root # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate
text==

Dans les lignes sivantes nous avons définie un certain nombre de varaibles, mais seules quelqu'unes sont
correctes, éliminez les lignes incorrectes.

bonjour=3
au revoir Ciao=3
byeBye7=3
6hello6=3
good_morning=3
good-afternoon=3
Hi!=3
oui=3
YES=3
def=3
_upem_=3

==

code==
bonjour=3
byeBye7=3
good_morning=3
oui=3
YES=3
_upem_=3
==


pltest==
>>> lines = [line.rstrip('\n') for line in open("student.py","r") ]
>>> len(lines) == 6  # il y a 6 expressions correctes dans le fichier
True
>>> 
==

feedback==
"au revoir Ciao" pas d'espace dans les noms
"6hello6" pas de chiffre en début d'identifieur
 "good-afternoon" le caractère "-" est un opérateur
 Les symboles "!=" sont le test de comparaison de différence donc "!" ne peut appraitre dans un identificateur
 La chaine "def" est un mot clef reservé du langage il n'est pas possible de l'utilisé comme identificateur
 ==

feedbackfalse==
Vous ne devez retirez que les lignes incorrectes.
==

 
