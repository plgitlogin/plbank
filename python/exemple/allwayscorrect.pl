# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz
template=/python/function/functiongradertemplate
title=allwayscorrect.pl
tag=test # N'oubliez pas de remplir ce champs svp
template=/python/fonction/functiongradertemplate
text==

*italic*
**bold**
***bold italic***

# section heading
## sub-section heading
### sub-sub-section heading

* first point
* second point
* third point

An [example link](http://example.com/ "Optional Title") in a sentence.

==

grader==
from functiongrader import doGood
doGood(feedback="ceci n'est pas un exercice doit être utilisé uniquement comme élement de test")
==

