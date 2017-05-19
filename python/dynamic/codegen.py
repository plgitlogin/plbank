

#opcompt=['<', '>', '<=', '<=' ,'==','!='] 
#opbool=['and','or']
#opint= ['-','*','+','/','//','%','**','>>','<<','&','|','^']

from random import randint,seed

tab="    "

class Essai2:
    def __init__(g,opint,opcomp, gseed):
        g.seed = gseed
        seed(gseed)
        g.currentindent=0
        g.opint = opint
        g.opcomp=opcomp
        g.interval=1
        g.funcs=[]
        g.farity=[]
        g.i=0
        g._and = True
        g._or = True
        g._if = True
        g._else = True
        g._elif = True
        g._func= True
    def callambda0(g,la):
        return la()
    def tabs(g):
        return g.currentindent*tab
    def op(g):
        return g.opint[randint(0,len(g.opint)-1)]
    def opcompt(g):
        return g.opcomp[randint(0,len(g.opcomp)-1)]
    def const(g):
        return str(randint(-g.interval,g.interval+1))
    def var(g,i):
        l=["foo","bar","i","nb","p","q","X","truc","_u_"]
        if i < len(l):
            return l[i]
        return "var"+str(i)
    def init(g,i):
        return g.var(i)+"= "+g.const()
    def randvar(g):
        return g.var(randint(0,g.i))
    def boolexp(g):
        r=randint(0,100)
        if r < 20:
            return g.randvar()+g.opcompt()+g.const()
        elif r <80:
            return g.randvar()+g.opcompt()+ g.randvar()
        else:
            if g._and and randint(0,10)>4:
                return g.boolexp()+" and "+ g.boolexp()
            elif g._or and randint(0,10)>4:
                return g.boolexp()+" and "+ g.boolexp()
            else:
                return g.randvar()+g.opcompt()+g.const()
                
    def instr(g,i):
        if randint(1,100)< 33:
            s= g.randvar()+"="+g.randvar()+" "+g.op()+" "+g.randvar()+"\n"
        elif randint(1,100)< 33:
            s= g.randvar()+"="+g.randvar()+" "+g.op()+" "+g.const()+"\n"
        elif g._if and g.currentindent < randint(1,3) :
            s="if "+g.boolexp()+":\n"
            g.currentindent += 1
            s+= g.currentindent*tab + g.instr(i)
            g.currentindent -= 1
            if g._elif and randint(1,100)< 33:
                s+= g.tabs()+"elif "+g.boolexp()+":\n"
                g.currentindent += 1
                s+= g.tabs() + g.instr(i)
                g.currentindent -= 1 
            if g._else and randint(1,100)< 44:
                s+= g.tabs()+"else:\n"
                g.currentindent += 1
                s+= g.tabs() + g.instr(i)
                g.currentindent -= 1
        else:
            return  g.randvar()+"="+g.randvar()+" "+g.op()+" "+g.const()+"\n"
        return s
    def printInits(g):
        for i in range(0,g.i):
            print(g.init(i))
    def code(g,nbv):
        s=""
        g.i=nbv
        for p in range(0,randint(2,5)):
            s+=g.instr(g.i)
        return s
    def buildFunc(g,n):
        # returning consts functions
        g.funcs.append("f")
        g.fatrity.append(0)
        return "def f():\n\treturn "+g.const()+"\n"
        # printing functions
        #      "def f():\n\tprint("+g.const()+")\n"
        # 
    def doit(g):
        s=""
        if g._func :
            s+=g.buildFunc(randint(1,2)) # une ou deux fonctions
            print(s,end="")
        s=g.code(3)
        g.printInits()
        print(s,end="")
        print(g.var(g.i)+"="+g.var(0)+"+"+g.var(g.i-2))
    def question(g):
        print('Quel est la valeur de la variable '+g.var(g.i)+" à la fin de l'execution")
    
gseed=randint(1,100)
x=Essai2(['+','*','-','%','/','//'],['<', '>', '<=', '<=' ,'==','!='],gseed=gseed)
x.doit()
x.question()
print("code:",gseed)
        
