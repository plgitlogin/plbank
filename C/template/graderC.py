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
    os.system(compilation_command + "> compilCstdout.log 2> compilCstderr.log ")
    
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
        dico_reponse["feedback"] = "Il y a des erreurs à la compilation de votre programme :<br /><br />Feedback gcc:<br />" + err_out
        return False
    # If there is some warnings
    if "warning:" in err_out:
        dico_reponse["feedback"] = "Vous pouvez augmenter la qualité de votre programme en lisant les recommandations du compilateur:<br /><br />Feedback gcc:<br />" + err_out
        dico_reponse["compilation"] = "warning"
    elif "warning:" in std_out:
        dico_reponse["feedback"] = "Vous pouvez augmenter la qualité de votre programme en lisant les recommandations du compilateur:<br /><br />Feedback gcc:<br />" + std_out
        dico_reponse["compilation"] = "warning"

    # No error, no warning
    else:
        if flags != "": # No quality cheching flag compilation
            dico_reponse["feedback"] = "Votre programme semble être écrit correctement (compilation avec "+flags+")<br />"
        else: # Some quality flags compilation
            dico_reponse["feedback"] = "Votre programme semble être écrit correctement<br />"
        dico_reponse["compilation"] = "parfaite"
    # Here, the compilation is OK with possible warnings
    return True

####################################
#         A single C test          #
####################################

def test_exec(name, in_args="", out_expected="", verbose=True):

    # set files for test arguments and expected output
    if in_args != "":
        file_stdin = open("args_in", "w")
        file_stdin.write(in_args)
        file_stdin.close()
    file_out_expected = open("out_expected", "w")
    file_out_expected.write(out_expected)
    file_out_expected.close()
    
    # execution and diff commands
    if in_args != "":
        test_command = "cat args_in | ./progCstudent > outputstudent"
    else:
        test_command = "./progCstudent > outputstudent"
    os.system(test_command)
    diff_command = "diff out_expected outputstudent > diffoutput"
    os.system(diff_command)
    file_diff = open("diffoutput", "r")
    content_diff = file_diff.read()
    file_diff.close()

    # In case of differences
    # TODO : Sure there is better solution than a unix diff
    if len(content_diff) > 0:
        # the test failled
        dico_reponse["feedback"] += "Le test " + name + " a échoué:<br />"
        # if there were arguments and activated verbose
        if in_args != "" and verbose:
            dico_reponse["feedback"] += "Pour les données <br />"
            dico_reponse["feedback"] += in_args + "<br />"
        # HINT: unactive verbose when arg or output are HHUUUGGEEEE !!!!
        if verbose:
            dico_reponse["feedback"] += "Attendu: <br />"
            dico_reponse["feedback"] += out_expected
            dico_reponse["feedback"] += "<br />Produit: <br />"
            file_out = open("outputstudent", "r")
            content_out = file_out.read()
            file_out.close()
            dico_reponse["errormessages"] += content_out
        return False
    # If the test pass and the verbose is activated
    else:
        if verbose:
            if in_args != "":
                dico_reponse["feedback"] += "<br />Pour les données<br />"
                dico_reponse["feedback"] += in_args
            dico_reponse["feedback"] += "Attendu: <br />"
            dico_reponse["feedback"] += out_expected
            dico_reponse["feedback"] += "<br />Produit: <br />"
            dico_reponse["feedback"] += out_expected           
    return True


####################################
#  ......:::: C grader ::::......  #
####################################

def grade(tests=dict(), flags=""):
    all_test_pass = True

    # We first try a no flag compilation in order to isolate errors only
    if not compile_gcc():
        # If the no flag compilation fails, GTFO
        print(json.dumps(dico_reponse))
        sys.exit()

    # Now, since it compiles, we try a compilation to get all 
    # warnings with the given flags
    compile_gcc(flags=flags)

    # time for tests !!!
    for test_name in tests:
        test_in = tests[test_name][0]
        test_out = tests[test_name][1]
        test_verbose = tests[test_name][2]
        if not test_exec(test_name, test_in, test_out, test_verbose):
            all_test_pass = False
            break # this break can be discussed for pedagogic reasons...
            # This break force students to solve mess one by one...
            # The guy who have all tests can solve them faster
            # But one by one, if you chose to fix mess with hacks, you
            # can be rapidly heading for a fall

    # The holy grail
    if all_test_pass:
        dico_reponse["errormessages"] = "Tous les tests passent..."
        dico_reponse["success"] = True

    # GTFO
    print(json.dumps(dico_reponse))
    sys.exit()
            
