#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  gifttopl.py
#  
#  Copyright 2017 Raihan BILAL <rbilal@u-pem.fr>
#  

'''gifttol.py
    Load Questions from gift file using the giftparser.py
    
    Creates one dictionnary per Question then writes new pl files in plbank and a new pltp containing them
'''

"""
pltpfromgift repertoiredestination giftfiles ...

creer des repertoire repertoirededestination/basename(gifile)/ contenant

un fichier basename(gitstfile).pltp et un pour chaque 


"""
import os
import sys
from os.path import basename, isdir, isfile, realpath, dirname
sys.path.append(os.path.dirname(__file__)+"/../../../server/serverpl/pysrc")
from giftparser import *
import re
import i18n
from copy import copy



def work(rel_path):
    res = list()
    try :
        with open(rel_path, 'r') as gift :
            questions = parseFile(gift)
            print(str(len(questions)) + " question(s) chargée(s)")
            for q in questions:
                d = q.toPl()
                if d:
                    res.append(d)
        return res
    except IOError as e:
        print("Impossible d'ouvrir le fichier : " + str(rel_path))
        return None


def create_pl(dicts, dest_path, pltp):
    '''
        Création pour chaque dictionnaire dans une liste de dictionnaire d'un fichier .pl
        Ecriture dans le .pl sous la forme :
        clef==
        valeur
        ==
        
        :param dicts : Une liste de dictionnaire
        :type dicts: List of dict
    '''
    list_res = list()
    for d in dicts :
        with open(dest_path+pltp+"/"+ d['name'] +".pl", 'w') as pl :
            for k in d.keys():
                if k == 'template':
                    print(str(k) +"="+str(d[k]), file=pl)
                elif k == 'type':
                    print(str(k) +"="+str(d[k]), file=pl)
                else:
                    print(str(k) +"==\n"+str(d[k])+"\n==", file = pl)
            list_res.append(str(pl.name.split('/')[-1]))
    for pl in list_res : print(pl)
    return list_res

def create_pltp(dicts, dest_path, pltp_name):
    '''
        Création des pl puis creation d'un pltp qui les référence tous
        :param dicts : Une liste de dictionnaire
        :type dicts: List of dict
    '''
    #If a pltp have already this name, we add a number to the name
    nouveau_pltp = (dest_path + pltp_name)
    try:
        os.mkdir(nouveau_pltp)
    except FileExistsError:
        n = 2
        while isdir(nouveau_pltp + str(n)):
            n+=1
        os.mkdir(nouveau_pltp + str(n))
        pltp_name = pltp_name + str(n)
    except OSError as e:
        print(type(e))
        print(str(e) + "impossible de créer le dossier")
        print(nouveau_pltp)
        sys.exit(1)
    pl_names = create_pl(dicts, dest_path, pltp_name)

    with open(dest_path + "%s/%s.pltp"%(pltp_name, pltp_name), 'w') as pltp:
        print("title=" + pltp_name.replace("_", " "), file = pltp)
        print("concept==gift", file = pltp)
        for plname in pl_names :
            print("@ /gift/%s/"%(pltp_name)+plname, file = pltp)
        print("==", file=pltp)


'''
def main(args):
    gift_dir = os.getcwd()
    dest_dir =  gift_dir.copy
    os.chdir(dirname(realpath(__file__)))
    
    #adding a slash if necessary
    if not (args[1][-1] == '/'):
        args[1] += '/'
        
    #si ce n'est pas un chemin absolu qui est renseigné
    if (args[1][0] == '/'):
        dest_dir = args[1]
    else:
        dest_dir += '/'+args[1]

    #si ce n'est pas un chemin absolu qui est renseigné
    if (args[2][0] == '/'):
        gift_dir = args[2]
    else:
        gift_dir += '/'+args[2]

    dicts = work(gift_dir)

    print("gift dir is : "+gift_dir)
    print("dest dir is : "+dest_dir)
    
    if dicts :
        create_pltp(dicts, dest_dir, basename(gift_dir).split(".")[0])
'''

if __name__ == '__main__':
    
    if (len(sys.argv) <= 2):
        print("Error : Too few arguments!")
        sys.exit(1)
    
    if not isdir(sys.argv[1]):
        print("Error : first argument must be a repository")
        sys.exit(1)

    #adding a slash if necessary
    if not (sys.argv[1][-1] == '/'):
        sys.argv[1] += '/'
    '''
    from itertools import takewhile, dropwhile
    print(sys.argv)
    bon = list(takewhile(lambda i: i.endswith(".gift"), sys.argv))
    print(bon)
    '''
    prefix_dir = os.getcwd()
    if sys.argv[1][0] == '/':
        dest_dir = sys.argv[1]
    #si ce n'est pas un chemin absolu qui est renseigné
    else:
        dest_dir = prefix_dir +'/'+ sys.argv[1]
        
    for i in range(2, len(sys.argv)):
        if (sys.argv[i][0] == '/'):
            gift_dir = sys.argv[i]
        #si ce n'est pas un chemin absolu qui est renseigné
        else:
            gift_dir = prefix_dir + '/'+sys.argv[i]

        dicts = work(gift_dir)

        if dicts :
            create_pltp(dicts, dest_dir, basename(gift_dir).split(".")[0])
