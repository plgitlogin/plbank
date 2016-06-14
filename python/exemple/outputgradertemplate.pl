# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
title=outputgradertemplate.pl



tag=root # N'oubliez pas de remplir ce champs svp

text==

MODIFIER

==

files=@/python/exemple/pldoctest.py
files=@/python/exemple/pldicjson.py
files=@/python/exemple/autograder.py



grader==
from autograder import testoutput
testoutput() 
==


