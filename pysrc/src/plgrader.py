

from feedback import Feedback
import subprocess

import json
def getOutput(inputstr=None):
    # FIXME
    pass



class Grader:
    def __init__(self):
        try:
            self.pld= json.load(open("pl.json","r"))
        except Exception as e:
            pldicsingleton = {"plateforme":False,
                "stderr":e,"result":False,
                "stdout":"PlateForme IO ERROR can't open pl.json"}
            print(json.dump(pldicsingleton))
            sys.exit(1)
        self.fb = Feedback()
        self.success=True

    def compilestudent(self):
            EEE=None

            import py_compile
            try:
                x= py_compile.compile("student.py",doraise=True)
                
            except Exception as EE:
                self.fb.addCompilationError(str(EE))
                self.success=False
                return False
            else:
                return True # compilation ok

    def doOutput(self):
        dico_response = { "success": self.success , "errormessages" : "","feedback": self.fb.feedback(), "other": "","error":"","execution": "","grade":"1"}
        return(json.dumps(dico_response))

    def expectedoutput(self):
        if not "expectedoutput" in self.pld:
            return False
        expected = self.pld["expectedoutput"]
        self.compareExpectedOutput(expected)
        return True

    def compareExpectedOutput(self,expected,stdinput=None):
        """
        Compare the output from student to expected argument
        update feedback in consequence
        return True if sucessfull
        """
        r,t = self.getStudentOutput()
        if r and t == expected :
            self.fb.addOutput(expected)
            self.fb.success = True
        else:
            self.fb.addExpectedOptained(t, expected)
            self.fb.success = False
        return self.fb.success

    def getStudentOutput(self, stdinput=None):
        # execute student.py
        return self.execute(["python3","student.py"],instr=stdinput)

    def getSoluceOutput(self,stdinput=None):
        return self.execute(["python3","student.py"],instr=stdinput)

    def execute(self,args,instr):
        try:
            if instr :
                encoded = stdinput.encode("utf-8")
            else:
                encoded = None
            tt = subprocess.check_output(args,input=encoded)
            return (True,tt.decode("utf-8"))
        except subprocess.CalledProcessError as cpe:
             return (False,cpe.stdout.decode("utf-8"))

    def inputoutput(self):
        if  not "output0" in self.pld:
            return False
        si="input0"
        so="output0"
        i= 0
        while si in self.pld and so in self.pld:
            r = self.compareExpectedOutput(self.pld[so],
                    stdinput=self.pld[si].encode("utf-8"))
            print("WWW"+str(r))
            if not r:
                return True
            i=i+1
            si="input"+str(i)
            so="output"+str(i)
        return True

    def grade(self):
        """
        compile
        expectedoutput ?
        input/output
        input/soluce
        inputgenerator/soluce
        pltest
        """
        if not self.compilestudent():
            return self.doOutput()
        elif self.expectedoutput() :
            return self.doOutput()
        elif self.inputoutput():
            return self.doOutput()
        # Default response should by an plateforme error
        # or a good answer to pass to next exercice
        if "author" in self.pld:
            self.fb.addFeedback("<H1> Problème exercice mal défini </H1> Contacter l'auteur: "+self.pld["author"]+"\n Passez à l'exercice suivant.")
        else:
            self.fb.addFeedback("<H1> Problème exercice mal défini </H1>Contacter l'auteur, ou l'administrateur \n Passez à l'exercice suivant.")
        return self.doOutput()
