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

dico_reponse = { "success": True , "errormessages" : "" , "execution": "Plateforme Error", "feedback": "", "other": "" }

def compiletest(ldflags=""):
    # Compilation command
    compilation_command = "gcc basic.c -o progCstudent"+ ldflags

    # Ugly : two times the compilations and constitution of two log files
    os.system(compilation_command + "1> compilCstdout.log")
    os.system(compilation_command + "2> compilCstderr.log")
    err_out_log = open("compilCstderr.log", "r")
    err_out = err_out_log.read()

    # If there is some compilation errors
    if len(err_out) > 0: # TODO : find a better python test for testing if a file is empty
        dico_reponse["success"] = False
        dico_reponse["errormessages"] = "Voir le feedback donné par le compilateur gcc"
        dico_reponse["execution"] = "Impossible"
        dico_reponse["feedback"] = "Il y a des erreurs à la compilation de votre programme :\n" + err_out
        err_out_log.close()
        return False

    err_out_log.close()
    std_out_log = open("compilCstdout.log", "r")
    std_out = std_out_log.read()

    if len(std_out) > 0: # TODO : find a better python test for testing if a file is empty
        dico_reponse["feedback"] = "Vous pouvez augmenter la qualité
        de votre programme en lisant les recommandations du
        compilateur:\n" + std_out

    # Here, the compilation is OK with possible warnings
    std_out_log.close()
    return True

def compilC():
    compiletest()
    print(json.dumps(dico_reponse))
    sys.exit()
