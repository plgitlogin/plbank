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
#        Get the exercice content                                        #
##########################################################################

dico_reponse = { "success": False , "errormessages" : "" ,
                 "execution": "Plateforme Error", "feedback": "",
                 "other": "", "compilation" : "erreur" }

exercice = json.load(open("pl.json","r"))

###################################################
#               Source embedding                  #
###################################################

def embed_code(path_src):
    """
    If some cases, just a fonction is required for an exercice. And a
    single function does not constitute a complete C program. To complete
    the program, the exercice quand provide a markdon bloc nammed
    'codecontext' which contains the context to form a practical program.

    This function update the C code inside the file `path_src` with
    the contectual code in the exercice if it exist.
    """
    if 'codecontext' in exercice and len(exercice['codecontext']) > 0:
        file_src = open(path_src, "r")
        old_content = file_src.read()
        file_src.close()

        new_content = exercice['codecontext'] + old_content
        file_src = open(path_src, "w")
        file_src.write(new_content)
        file_src.close()

    if 'codecontextafter' in exercice and len(exercice['codecontextafter']) > 0:
        file_src = open(path_src, "r")
        old_content = file_src.read()
        file_src.close()

        new_content = old_content + exercice['codecontextafter']
        file_src = open(path_src, "w")
        file_src.write(new_content)
        file_src.close()

# Code contextual
embed_code("basic.c")

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
            out_expected = "<br />".join(out_expected.split("\n"))
            dico_reponse["feedback"] += out_expected
            dico_reponse["feedback"] += "<br />Produit: <br />"
            file_out = open("outputstudent", "r")
            content_out = file_out.read()
            file_out.close()
            content_out = "<br />".join(content_out.split("\n"))
            dico_reponse["feedback"] += content_out + "<br />"
        # The test failed so we return False
        return False
    # If the test pass and the verbose is activated
    else:
        if verbose:
            if in_args != "":
                dico_reponse["feedback"] += "<br />Pour les données<br />"
                dico_reponse["feedback"] += in_args
            dico_reponse["feedback"] += "Attendu: <br />"
            out_expected = "<br />".join(out_expected.split("\n"))
            dico_reponse["feedback"] += out_expected
            dico_reponse["feedback"] += "<br />Produit: <br />"
            dico_reponse["feedback"] += out_expected + "<br />"
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
    file_soluce = open("sources_soluce.c", "w")
    file_soluce.write(exercice['codecmp'])
    file_soluce.close()

    # code contextual
    embed_code("sources_soluce.c")

    # We compile the soluce program.
    cmd_gcc = "gcc -o progCsoluce sources_soluce.c " + flags_soluce
    os.system(cmd_gcc)

    output_tests = dict()
    for name in tests:
        # set files for test arguments and expected output
        # execution and diff commands
        cmd_args = tests[name][0]
        in_args = tests[name][1]
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

        output_tests[name] = [cmd_args, in_args, out_expected, tests[name][2]]

    grade_argcmd_stdin_stdout(output_tests, flags=flags, break_first_error=break_first_error)

####################################################################
#               A class for a single C unitary test                #
####################################################################

class C_unit_test():
    """
    A class for unitary tests of a C programm. The arguments are :

    * name : a name for the test

    * command_args : a long string of arguments given to the
      executable (space separate arguments)

    * sdtin : a stream given during programm execution on the standard
      input

    * expected_output : fusion of standard output and standard error
      output (i.e. what produce the C programm in output if launched
      in a terminal)

    * executable_path : a path to the exuctable (mainly its name)
    """
    def __init__(self, name, command_args="", sdtin="",
                 expected_output="", executable_path=None):
        """
        Initialization of `self`.
        """
        self._name = name
        self._command_args = command_args
        self._stdin = sdtin
        self._expected_output = expected_output
        self._executable_path = executable_path

        self._output_path = "output.log"
        self._stdin_path = "stdin.log"
        self._feedback = ""
        self._result = None

    def __str__(self):
        """
        Return a single string to describe `self` (returns mainly the
        name of the test).
        """
        return "Test {}".format(self._name)

    def programm_path(self):
        """
        Return the path (mainly the name) of the C executable.
        """
        return self._executable_path

    def command_args(self):
        """
        Return the string consisting of arguments given to the
        executable for the test `self`.
        """
        return self._command_args

    def stdin(self):
        """
        Return the content given into the standard input to launch the
        test `self`.
        """
        return self._stdin

    def stdin_path(self):
        """
        Return the path of the file containing the standard input text
        for the test `self`.
        """
        return self._stdin_path

    def output_path(self):
        """
        Return the name of the file containing output of the test
        """
        return self._output_path

    def command_test(self):
        """
        Return the command use to execute the test `self`.
        """
        if len(self.stdin()) > 0:
            cmd = "cat {} | ./{} " + self.command_args() + " > {}".format(self.stdin_path(),
                                                                          self.programm_path(),
                                                                          self.output_path())
        else:
            cmd = "./{} " + self.command_args() + " > {}".format(self.programm_path(),
                                                                 self.output_path())
        return cmd

    def expected_output(self):
        """
        Return the expected output of the test `self` as a long text
        string.
        """
        return self._expected_output

    def feedback(self):
        """
        Return brut text feedback for the test `self`.
        """
        if self._result is not None:
            return self._feedback
        else:
            self.run_test()
            return self._feedback

    def result(self):
        """
        Return the result of the test `self`. Lanch the test if the result
        """
        if self._result is not None:
            return self._result
        else:
            self.run_test()
            return self._result

    def run_test(self):
        """
        Run the test `self`. A call to this method update the feedback
        and the result of the test. You should normally never call
        this method yourself. Asking for the result of the test or the
        feedback of the test will automatically run only once this test.

        This method caches the results. So, it is supposed to be called
        only a single time.
        """
        cmd = self.command_test()
        os.system(cmd)

        # Place expected output in file expected_output.log
        expected_output_file = open("expected_output.log", "w")
        expected_output_file.write(self.expected_output())
        expected_output_file.close()

        # Place sdtin inside a file
        if len(self.stdin()) > 0:
            stdin_file = open(self.stdin_path(), "w")
            stdin_file.write(self.stdin())
            stdin_file.close()

        diff_cmd = "diff {} {} > {}".format("expected_output.log", self.output_path(), "diff_output.log")
        # read the diff
        diff_output_file = open("diff_output.log", "r")
        diff_output = diff_output_file.read()
        diff_output_file.close()

        # read the output produced by execution to generate feedback
        output_exec_file = open(self.output_path(), "r")
        output_exec = output_exec_file.read()
        output_exec_file.close()

        # Update result of the test
        if len(diff_output) == 0:
            self._result = True
            feedback = "Test {} ... OK\n".format(self._name)
        else:
            self._result = False
            feedback = "Test {} ... echec\n".format(self._name)

        # contextual information for this test
        if self.command_args() != "":
            feedback += "Arguments : {}\n".format(self.command_args())
        if self.stdin() != "":
            feedback += "Entrée clavier : {}\n".format(self.stdin())
        feedback += "Réponse attendue : \n{}\n".format(self.expected_output())
        feedback += "Réponse obtenue : \n{}\n".format(output_exec)

        # Update the feedback
        self._feedback = feedback


####################################################################
#            A class for an ordered list of C tests                #
#            (we know expected ouput for each test)                #
####################################################################

class Play_tests():
    """
    A class for an ordered lists of tests.

    (string for test name,
     arguments in command line,
     stdin of test,
     output of test,
     verbose for the test)
    """
    def __init__(self, tests, executable_path):
        self._tests = tests
        self._executable_path = executable_path
        self._feedback = ""
        self._result = None

    def __str__(self):
        return "A collection of {} test(s)".format(len(tests))

    def tests(self):
        """
        Return the list of tests inside
        """
        return self._tests

    def executable_path(self):
        """
        Return the path of the tested executable.
        """
        return self._executable_path

    def result(self):
        """
        Return the state of execution of all test contained in
        `self`. It return `True` if all test pass and `False`
        otherwise.
        """
        if self._result is not None:
            return self._result
        else:
            self.run_tests()
            return self._result

    def feedback(self):
        """
        Return brut text feedback for the all tests contained in `self`.
        """
        if self._result is None:
            self.run_tests()
        return self._feedback

    def run_tests(self):
        # be positive at first glance
        all_test_pass = True

        # for each test inside the list (which is ordered...)
        for test in self.tests():
            test_name = test[0]
            cmd_arg = test[1]
            stdin = test[2]
            expected_output = test[3]

            test_instance = C_unit_test(test_name, cmd_arg, stdin, expected_output, self.executable_path())
            if not test_instance.result():
                all_test_pass = False
            self._feedback += test_instance.feedback()

        # The holy grail
        self._result = all_test_pass
        if all_test_pass:
            self._feedback += "Tous les tests passent...\n"
        else:
            self._feedback += "Identifier scrupuleusement les conditions de test qui échouent pour corriger votre code.\n"
