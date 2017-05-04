# Copyright 2016 Nicolas Borie <nicolas.borie@u-pem.fr>
author=Nicolas Borie
name=Premier programme en C
title=Premier programme en C
tag=output
template=/C/template/autograderC

text==
Faites votre premier programme C, ce programme devra écrire *Hello
World!* sur la sortie standard et retourner à la ligne.
==

code==
#include <stdio.h>

int main(int argc, char* argv[]){
/* votre code ici... */
}
==

soluce==
#include <stdio.h>

int main(int argc, char* argv[]){
  printf("Hello World\n");
  return 0;
}
==

expectedoutput==
Hello World!
==

# chargement des fichiers utiles 
files=@/C/template/basic.c
files=@/C/template/graderC.py

grader==
from graderC import grade
grade( {"simple éxécution": ["", "Hello World!\n", True]} )
==
