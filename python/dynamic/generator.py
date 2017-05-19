#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generator.py
#  
#  Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
#  
# 

import codegen
from random import randint
"""creation d'un template pour le code avec des variables varN   avec N=1,2,...
en suite render du template avec des nom plus aléatoires"""


def randfromlist(l):
    """
    >>> randfromlist([0])
    0
    >>> randfromlist([0,0,0,0,0])
    0
    """
    return l[randint(0,len(l)-1)]


class Generator:
    def __init__(generator):
        generator.currentindent=0
        generator.code="" # main code 
        generator.inits="" # creation des fonctions et variables
        generator.varid=1 # première variable s'appel var1
        generator.funid=1 # la première function s'appel fun1
    def randopint(generator):
        return  randfromlist(generator.opint)
    def addcode(generator,line):
        generator.code += "\t"*generator.currentindent+line+"\n"
    def incIndent(generator):
        generator.currentindent += 1
    def decIndent(generator):
        generator.currentindent -= 1
    def randinit(generator,const):
        """
        const | const randopint() randint(1,3) | funN(const) 
        """
    def addInits(generator,id):
        generator.inits += "{{- var"+id + "}}=" + generator.randinit(generator.randconstante())+"\n"

    def instructions(generator):
        """
        retourne une instruction 
        """


def main(args):
    # define limites
    #
    #opcompt=['<', '>', '<=', '<=' ,'==','!='] 
    #opbool=['and','or']
    #opint= ['+','-','*','/','//','%','**','>>','<<','&','|','^']
    #linst= ["if 
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
