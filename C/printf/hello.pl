# Copyright 2016 Nicolas Borie <nicolas.borie@u-pem.fr>
author=Nicolas Borie
name=Premier programme en C
title=Premier programme en C
tag=
template=/C/template/autograderC

text==
Faites votre premier programme C, ce programme devra écrire *Hello
World* sur la sortie standard et retourner à la ligne.
==

code==
#include <stdio.h>

/* main est la fonction principale d'un programme. C'est la fonction
qui sera appelé lors de l'éxecution du programme. argc et argv sont
les arguments typés du programme, on verra plus tard comment les
utiliser.*/
int main(int argc, char* argv[]){
/* votre code SVP */
}
==

soluce==
#include <stdio.h>

int main(int argc, char* argv[]){
  print("Hello World\n");
  return 0;
}
==

expectedoutput==
Hello World
==

# chargement des fichiers utiles 
files=@/C/template/basic.c
files=@/C/template/compilCsoft.py

grader==
from compilCsoft import compilC
compilC()
==
