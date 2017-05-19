# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=impots.pl
title= Calcul de l'impot   # N'oubliez pas de remplir ce champs svp
tag=fonctions|list
template=/python/template
text=@impots.md

files=@patate

# Choisir pltest ou soluce ou expectedoutput

pltest==
>>> calcul(0,5)
0
>>> calcul(12000,1)
321
>>> calcul(1200000,4)
461402
>>> tauxglobal(78000,2.5)
12
>>> exemples([(8899,1)])
Pour un revenu imposable de 8899 et 1 part(s) l'import est de 0 € et le taux global de 0 %.
>>> exemples([(88909,1)])
Pour un revenu imposable de 88909 et 1 part(s) l'import est de 22894 € et le taux global de 26 %.
>>> exemples([(88909,1),(56789,2.5)])
Pour un revenu imposable de 88909 et 1 part(s) l'import est de 22894 € et le taux global de 26 %.
Pour un revenu imposable de 56789 et 2.5 part(s) l'import est de 4552 € et le taux global de 8 %.
>>> exemples([(88909,1),(78000,2.5)])
Pour un revenu imposable de 88909 et 1 part(s) l'import est de 22894 € et le taux global de 26 %.
==

testcode=@calculimpots.py
