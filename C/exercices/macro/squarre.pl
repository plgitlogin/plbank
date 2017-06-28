# Copyright 2016 Nicolas Borie <nicolas.borie@u-pem.fr>
#
# Macro à paramètre pour calculer un carré

author=Nicolas Borie
name=Macro pour calculer un carré
title=Macro pour calculer un carré
tag=macro
template=/C/template/autograderC

text==

Écrire une macro **SQUARRE** qui prend en argument un seul paramètre
(jamais typé comme c'est toujour le cas pour les macros) qui remplace
son argument par le carré de son paramètre. Le paramètre de la macro
sera toujours une expression C qui s'évalue dans un type numérique.

==

code==
#define SQUARRE....

==

codecmp==
#define SQUARRE(a) ((a)*(a))

==

codecontext==
#include <stdio.h>

int main(int argc, char* argv[]){

  printf("Le carré de %d est %d\n", 0, SQUARRE(0));
  printf("Le carré de %d est %d\n", 1, SQUARRE(1));
  printf("Le carré de %d est %d\n", 12, SQUARRE(12));
  printf("Le carré de %s est %d\n", "1+2", SQUARRE(1+2));
  printf("Le carré de %s est %d\n", "2-1", SQUARRE(2-1));
  printf("Le carré de %f est %f\n", 3.14, SQUARRE(3.14));
  return 0;
}

==

# LOAD IMPORTANT FILES FOR GRADING
files=@/C/template/basic.c
files=@/C/template/graderC.py

grader==
from graderC import grade_argcmd_stdin_cmp_soluce
tests = {"expressions classiques": ["","", True]}
grade_argcmd_stdin_cmp_soluce(tests=tests, flags="-Wall -ansi", break_first_error=True, flags_soluce="-Wall -ansi")
==
