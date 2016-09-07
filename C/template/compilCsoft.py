#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  compilCsoft.py
#  
#  Copyright 2016 Nicolas Borie <nicolas.borie@u-pem.fr>
#  

########################################################
#  Compilation de programme C avec le compilateur gcc  #
########################################################

import os
import sys
import json 

############################################
#  Ajout d'un champ compilation pour le C  #
############################################

dico_reponse = { "success": True , "errormessages" : "" ,
                 "execution": "Plateforme Error", "feedback": "", 
                 "other": "", "compilation" : "erreur" }

def compiletest(ldflags=""):
    # Compilation command
    compilation_command = "gcc basic.c -o progCstudent "+ ldflags

    os.system(compilation_command + " 2> compilCstderr.log")
    err_out_log = open("compilCstderr.log", "r")
    err_out = err_out_log.read()
    err_out_log.close()

    # If there is some compilation errors
    if "error:" in err_out:
        dico_reponse["success"] = False
        dico_reponse["errormessages"] = "Voir le feedback donné par le compilateur gcc"
        dico_reponse["execution"] = "Impossible"
        dico_reponse["feedback"] = "Il y a des erreurs à la compilation de votre programme :\n" + err_out
        return False

    # If there is some warnings
    if "warning:" in err_out:
        dico_reponse["feedback"] = "Vous pouvez augmenter la qualité de votre programme en lisant les recommandations du compilateur:\n" + err_out
        dico_reponse["compilation"] = "warning"
    # No error, no warning
    else:
        dico_reponse["feedback"] = "Votre programme semble être écrit correctement\n"
        dico_reponse["compilation"] = "parfaite"
    # Here, the compilation is OK with possible warnings
    std_out_log.close()
    return True

def compilC():
    # We first try a no flag compilation
    if not compiletest():
        print(json.dumps(dico_reponse))
        sys.exit()
    # Now, we try a -Wall -ansi compilation
    compiletest("-Wall -ansi")
    print(json.dumps(dico_reponse))
    sys.exit()
            
