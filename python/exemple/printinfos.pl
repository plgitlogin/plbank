# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=printinfos.pl
tag=root # N'oubliez pas de remplir ce champs svp
template=/python/function/functiongradertemplate
text==

Clicker sur check 

==

grader==

import sys
from functiongrader import doGood


doGood(execution=(sys.version_string+sys.pathdirs))


==

# files=@/python/pahtdufichier/nomdufichier
soluce==
# une solution de l'exercice
# utile pour les tests
==
