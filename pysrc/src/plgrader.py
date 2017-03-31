

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
            self.success =True
            self.feedback = "# erreur de plateforme \n pl.json illissible\n"
            self.doOutput()
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
        stdinput = self.pld["input0"] if "input0" in self.pld else None
        self.compareExpectedOutput(expected,stdinput)
        return True

    def compareExpectedOutput(self,expected,stdinput=None):
        """
        Compare the output from student to expected argument
        update feedback in consequence
        return True if sucessfull
        """
        r,t = self.getStudentOutput(stdinput)
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

    def getSoluceOutput(self, stdinput=None):
        r,out = self.execute(["python3","soluce.py"],instr=stdinput)
        if not r:
            self.fb.addFeedback("Problemes with the soluce")
            self.fb.addFeedback(out)
        return (r,out)

    def execute(self,args,instr):
        try:
            if instr :
                encoded = instr.encode("utf-8")
            else:
                encoded = None
            tt = subprocess.check_output(args,input=encoded,
                                stderr=subprocess.STDOUT)
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
            self.fb.asio=True
            self.fb.addInput(self.pld[si])
            r = self.compareExpectedOutput(self.pld[so],
                    stdinput=self.pld[si])
            if not r:
                return True
            i=i+1
            si="input"+str(i)
            so="output"+str(i)
        return True

    def inputsoluce(self):
        if  not "soluce" in self.pld:
            return False
        si="input0"
        i= 0
        while si in self.pld :
            self.fb.asio=True
            self.fb.addInput(self.pld[si])
            r,soloutput = self.getSoluceOutput(stdinput=self.pld[si])
            if not r:
                return False
            r = self.compareExpectedOutput(soloutput,
                    stdinput=self.pld[si])
            if not r:
                return True
            i=i+1
            si="input"+str(i)
        return True

    def getrandomgenerated(self,num):
        r,out = self.execute(["python3","inputgenerator.py",str(num)],None)
        if not r:
            self.fb.addFeedback("Problemes with the input generator ")
            self.fb.addFeedback(out)
        return (r,out)

    def generatorsoluce(self):
        if  not "soluce" in self.pld or not "inputgenerator" in self.pld:
            return False
        if "numberofgenerator" in self.pld:
            num=int(self.pld["numberofgenerator"])
        else:
            num=4
        self.fb.showinput = True # random ...
        for x in range(num):
        
            self.fb.asio=True
            r,stdinput = self.getrandomgenerated(x)
            if not r:
                return False
            r,soloutput = self.getSoluceOutput(stdinput=stdinput)
            if not r:
                return False
            r = self.compareExpectedOutput(soloutput,
                    stdinput=stdinput)
            if not r:
                return True
        return True

    def dopltest(self):
        if not "pltest" in self.pld :
            return False
        try:
            with open("pltest.py","w") as pltf :
                with open("student.py","r") as f:
                    print("\"\"\"\n"+self.pld["pltest"]+">>> \n\"\"\"",file=pltf)
                    print(f.read(),file=pltf)
        except Exception as e:
           return False

        import os
        os.environ['TERM']="linux"# bug in readlinehttps://bugs.python.org/msg191824
        r,out=self.execute(['python3','-B','-m','doctest','-f','-v','pltest.py'],instr=None)
        self.success = r
        if r :
            self.fb.addFeedback("# Tests\n")
            self.fb.addFeedback(out)
        else:
            self.fb.addOutput("# Echec de tests\n")
            self.fb.addOutput(out)
        return True

    def grade(self):
        """
        compile
        expectedoutput ?
        input/output
        input/soluce
        inputgenerator/soluce
        input/soluce
        pltest
        """
        if not self.compilestudent():
            return self.doOutput()
        elif self.expectedoutput() :
            return self.doOutput()
        elif self.inputoutput():
            if "showinput" in self.pld and self.pld['showinput']:
                self.fb.showinput=True
            return self.doOutput()
        elif self.generatorsoluce():
            return self.doOutput()
        elif self.inputsoluce():
            return self.doOutput()
        elif self.dopltest():
            return self.doOutput()
        # Default response should by an plateforme error
        # or a good answer to pass to next exercice
        if "author" in self.pld:
            self.fb.addFeedback("<H1> Problème exercice mal défini </H1> Contacter l'auteur: "+self.pld["author"]+"\n Passez à l'exercice suivant.")
        else:
            self.fb.addFeedback("<H1> Problème exercice mal défini </H1>Contacter l'auteur, ou l'administrateur \n Passez à l'exercice suivant.")
        return self.doOutput()
