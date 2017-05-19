# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=template de grader pour le C
title= template de grader pour le C   # N'oubliez pas de remplir ce champs svp
tag=  # N'oubliez pas de remplir ce champs svp
template=/C/template


file@=/C/template/basic.c
file@=/C/template/cgrader.bash

grader==

import os
os.system("cgrader.bash")
==

