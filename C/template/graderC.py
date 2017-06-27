#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Copyright 2016 Nicolas Borie <nicolas.borie@u-pem.fr>
#

##########################################################################
#           ...::: Classsical graders for the C langage :::...           #
##########################################################################
#
# Different use cases :
#
# --> We have a collection of tests with :
#     * arguments for the program
#     * stdin content
#     * expected output
#
# --> We have a solution and a collection of tests with :
#     * arguments for the program
#     * stdin content
#     (We auto-generate expected output using the solution)
#
# --> Embedding code :
#     The exercie consist in implementing only a fonction.
#     The exercice embbed the student code inside a program
#     for the tests
#
# --> Fill me if relevant....
#


import os
import sys
import json

##########################################################################
#  Initialization of dico_reponse add a champ compilation for C langage  #
##########################################################################

dico_reponse = { "success": False , "errormessages" : "" ,
                 "execution": "Plateforme Error", "feedback": "",
                 "other": "", "compilation" : "erreur" }

###################################################
#  Compilation for C programms with gcc compiler  #
###################################################

def compile_gcc(flags=""):
    """
    This fonction take in argument compilation and linking flags and
    generate from the student C sources `basic.c` a program
    `progCstudent`. This function uses the `gcc` compiler.

    This function upadte two field of the dictionary `dico_reponse`.
    Field `compilation` is set to :
    - `error` if an error appears during compilation
    - `warning` if `gcc` suggests a possible improvements of the sources
    - `perfect` if the source check fully compilation standards

    The field `feedback` is also setted with gcc answer when relevant.
    """

    # Compilation command
    compilation_command = "gcc basic.c -o progCstudent "+ flags

    # Execution in terminal
    os.system(compilation_command + "> compilCstdout.log 2> compilCstderr.log ")

    # Get back the standard/error output of compilation
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
        dico_reponse["feedback"] = "Il y a des erreurs à la compilation de votre programme :<br /><br />Feedback gcc:<br />" + err_out + "<br />"
        dico_reponse["compilation"] = "erreur"
        # No programm has been produced so this is the only case for
        # which we return False
        return False

    # If there is some warnings in standard error (it happen...)
    if "warning:" in err_out:
        dico_reponse["feedback"] = "Vous pouvez augmenter la qualité de votre programme en lisant les recommandations du compilateur:<br /><br />Feedback gcc:<br />" + err_out + "<br />"
        dico_reponse["compilation"] = "warning"

    # Sometimes warnings are thrown by standard output
    elif "warning:" in std_out:
        dico_reponse["feedback"] = "Vous pouvez augmenter la qualité de votre programme en lisant les recommandations du compilateur:<br /><br />Feedback gcc:<br />" + std_out + "<br />"
        dico_reponse["compilation"] = "warning"

    # No error, no warning
    else:
        if flags != "": # No quality cheching flag compilation
            dico_reponse["feedback"] = "Votre programme semble être écrit correctement (compilation avec "+flags+")<br />"
        else: # Some quality flags compilation
            dico_reponse["feedback"] = "Votre programme semble être écrit correctement<br />"
        dico_reponse["compilation"] = "perfect"

    # Here, the compilation is OK with possible warnings
    return True


#######################################################################
#     A single C test with command arg, stdin and expected stdout     #
#######################################################################

def test_exec(name, cmd_args="", in_args="", out_expected="", verbose=True):
    """
    Execute the student program (nammed `progCstudent`) giving it
    `cmd_args` arguments in command line, `in_args` in standard input
    and checking its standard output with out_expected.

    The standard streams are managed with unix redirection. Output
    of the student programm and expected output are compared with
    the Unix `diff` utility. If the returned `diff` is cleaned,
    the test is considered as valid. The test failed if this `diff`
    id non trivial.

    The field `feedback` of the dictionnary `dico-reponse`
    is updated by this function. According the `verbose`
    (activated or not), extra information is added inside the
    feedback for debugging.
    """

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
        test_command = "cat args_in | ./progCstudent " + cmd_args  + " > outputstudent"
    else:
        test_command = "./progCstudent " + cmd_args + " > outputstudent"
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
        dico_reponse["feedback"] += "Le test " + name + " a échoué<br />"
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
            dico_reponse["feedback"] += content_out
        # The test failed so we return False
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
    # At this point, the test passes.
    return True


###########################################################################
#     A single C test with comparaison to a teacher solution version      #
###########################################################################

def test_exec_cmp_soluce(name, cmd_args="", in_args="", verbose=True, flags_soluce=""):
    """
    Execute the student program (nammed `progCstudent`) giving it
    `cmd_args` arguments in command line, `in_args` in standard input
    and checking its standard output with a solution provide by the
    author of the exercice.

    The standard streams are managed with unix redirection. Output
    of the student programm and expected output are compared with
    the Unix `diff` utility. If the returned `diff` is cleaned,
    the test is considered as valid. The test failed if this `diff`
    id non trivial.

    The field `feedback` of the dictionnary `dico-reponse`
    is updated by this function. According the `verbose`
    (activated or not), extra information is added inside the
    feedback for debugging.    
    """
    # Build the expected output using the teacher version.
    file_soluce = open("sources_soluce.c", "w")
    file_solcue.write(dico_reponse['soluce'])
    file_soluce.close()

    # We compile the soluce program.
    cmd_gcc = "gcc -o progCsoluce sources_soluce.c " + flags_soluce
    os.system(cmd_gcc)

    # set files for test arguments and expected output
    if in_args != "":
        file_stdin = open("args_in", "w")
        file_stdin.write(in_args)
        file_stdin.close()
        test_command = "cat args_in | ./progCsoluce " + cmd_args  + " > outputsoluce"
    else:
        test_command = "./progCsoluce " + cmd_args + " > outputsoluce"
    os.system(test_command)

    # Set now the expected output
    file_out_expected = open("outputsoluce", "r")
    out_expected = file_out_expected.read()
    file_out_expected.close()

    # Now, we call the usual one test fonction
    return test_exec(name, cmd_args=cmd_args, in_args=in_args, out_expected=out_expected, verbose=verbose)


##############################################################################
#              ......:::: C classicals grader ::::......                     #
##############################################################################


def grade_argcmd_stdin_stdout(tests=dict(), flags="", break_first_error=True):
    """
    This grader takes in arguments a dictionnary of tests nammed `tests`.
    Each record must be of this format :

    string for test name: (arguments in command line,
                           stdin of test,
                           output of test,
                           verbose for the test)

    This grader will compile the student source code producing an executable.
    The compiling and linking `flags` will be used during this process. Then,
    for each test inside the dictionnary,

    * `dico_reponse['feedback']` is updated by subfonction called.

    * `dico_reponse['success']` is setted to `True` if all tests pass.

    * Testing stop at first error... If `break_first_error` is setted
      to `False`, then all tests will be launched.
    """

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
        test_args = tests[test_name][0]
        test_in = tests[test_name][1]
        test_out = tests[test_name][2]
        test_verbose = tests[test_name][3]
        if not test_exec(test_name, test_args, test_in, test_out, test_verbose):
            all_test_pass = False
            if break_first_error:
                break

    # The holy grail
    if all_test_pass:
        dico_reponse["errormessages"] = "Tous les tests passent..."
        dico_reponse["success"] = True

    # GTFO
    print(json.dumps(dico_reponse))
    sys.exit()


def grade_argcmd_stdin_cmp_soluce(tests=dict(), flags="", break_first_error=True, flags_soluce="-Wall -ansi"):
    """
    This grader takes in arguments a dictionnary of tests nammed `tests`.
    Each record must be of this format :

    string for test name: (arguments in command line,
                           stdin of test,
                           verbose for the test)

    This grader compile the solution given in the exercice. Thus, fort
    each test, it compute its expected output. Once it is done, it use the 
    other grader `grade_argcmd_stdin_stdout`.
    """
    # Build the expected output using the teacher version.
    # file_soluce = open("sources_soluce.c", "w")
    # file_soluce.write(dico_reponse['soluce'])
    # file_soluce.close()

    dico_reponse['feedback'] += "<br />SOLUCE<br />"
    if 'soluce' in dico:
        dico_reponse['feedback'] += dico['soluce']
    else:
        dico_reponse['feedback'] += "NO SOLUCE"
    dico_reponse['feedback'] += "<br />CODE CONTEXT<br />"
    if 'codecontext' in dico:
        dico_reponse['feedback'] += dico['codecontext']
    else:
        dico_reponse['feedback'] += "NO CODE CONTEXT"
    dico_reponse["success"] = True

    # GTFO
    print(json.dumps(dico_reponse))
    sys.exit()

    
    # We compile the soluce program.
    cmd_gcc = "gcc -o progCsoluce sources_soluce.c " + flags_soluce
    os.system(cmd_gcc)

    output_tests = dict()
    for name in tests:
        # set files for test arguments and expected output
        # execution and diff commands
        cmd_args = test[name][0]
        in_args = test[name][1]
        if in_args != "":
            file_stdin = open("args_in", "w")
            file_stdin.write(in_args)
            file_stdin.close()
            test_command = "cat args_in | ./progCsoluce " + cmd_args  + " > outputsoluce"
        else:
            test_command = "./progCsoluce " + cmd_args + " > outputsoluce"
        os.system(test_command)

        # Set now the expected output
        file_out_expected = open("outputsoluce", "r")
        out_expected = file_out_expected.read()
        file_out_expected.close()    

        output_tests[name] = [cmd_args, in_args, out_expected, test[name][2]]

    grade_argcmd_stdin_stdout(output_tests, flags=flags, break_first_error=break_first_error)
