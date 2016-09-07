#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  compilCsoft.py
#  
#  Copyright 2016 Nicolas Borie <nicolas.borie@u-pem.fr>
#  

##################################################
#  Compilation of C programms with gcc compiler  #
##################################################

import os
import sys
import json 

############################################
#  Ajout d'un champ compilation pour le C  #
############################################

dico_reponse = { "success": False , "errormessages" : "" ,
                 "execution": "Plateforme Error", "feedback": "", 
                 "other": "", "compilation" : "erreur" }

###################################################
#  Compilation for C programms with gcc compiler  #
###################################################

def compile_gcc(flags=""):
    # Compilation command
    compilation_command = "gcc basic.c -o progCstudent "+ flags

    # TODO : avoid double compilation
    #
    # Here is the problem :
    # a missing inclusion produce a message on stderr 
    # (given by ld but gcc give it on stderr)
    # a single small warning (like reach end of main function 
    # without returned value) is on stdout
    #
    # Both are just warning (a valid executable is produced)
    # both are not on the same file descriptor
    os.system(compilation_command + " 2> compilCstderr.log")
    os.system(compilation_command + " 1> compilCstdout.log")
    err_out_log = open("compilCstderr.log", "r")
    err_out = err_out_log.read()
    err_out_log.close()
    std_out_log = open("compilCstdout.log", "r")
    std_out = std_out_log.read()
    std_out_log.close()

    # If there is some compilation errors
    if "error:" in err_out:
        dico_reponse["errormessages"] = "Voir le feedback donné par le compilateur gcc"
        dico_reponse["execution"] = "Impossible"
        dico_reponse["feedback"] = "Il y a des erreurs à la compilation de votre programme :\n" + err_out
        return False

    # If there is some warnings
    if "warning:" in err_out:
        dico_reponse["feedback"] = "Vous pouvez augmenter la qualité de votre programme en lisant les recommandations du compilateur:\n" + err_out
        dico_reponse["compilation"] = "warning"
    elif "warning:" in std_out:
        dico_reponse["feedback"] = "Vous pouvez augmenter la qualité de votre programme en lisant les recommandations du compilateur:\n" + std_out
        dico_reponse["compilation"] = "warning"

    # No error, no warning
    else:
        if flags != "": # No quality cheching flag compilation
            dico_reponse["feedback"] = "Votre programme semble être écrit correctement (compilation avec "+flags+")\n"
        else: # Some quality flags compilation
            dico_reponse["feedback"] = "Votre programme semble être écrit correctement\n"
        dico_reponse["compilation"] = "parfaite"
    # Here, the compilation is OK with possible warnings
    return True

####################################
#         A single C test          #
####################################

def test_exec(name, in_args="", out_expected=""):

    # set file for test arguments and expected output
    if in_args != "":
        file_stdin = open("args_in", "w")
    if out_expected != "":
        file_out_expected = open("out_expected", "w")

    


    # close file for test arguments and expected output
    if in_args != "":
        file_stdin.close()
    if out_expected != "":
        file_out_expected.close()


####################################
#  ......:::: C grader ::::......  #
####################################

def grade(tests=dict()):
    all_test_pass = True

    # We first try a no flag compilation in order to isolate errors only
    if not compile_gcc():
        # If the no flag compilation fails, GTFO
        print(json.dumps(dico_reponse))
        sys.exit()

    # Now, since it compiles, we try a -Wall -ansi compilation to get all 
    # warnings
    compile_gcc("-Wall -ansi")

    # time for tests !!!
    for test_name in tests:
        test_in = tests[test_name][0]
        test_out = tests[test_name][1]
        if not test_exec(test_name, test_in, test_out):
            all_test_pass = False

    if all_test_pass:
        dico_reponse["success"] = True

    # GTFO
    print(json.dumps(dico_reponse))
    sys.exit()
            
