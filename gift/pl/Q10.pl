type==
direct
==
name==
Q10
==
title==
Q10
==
text==
What two people are entombed in Grant's tomb?
==
sandbox==
False
==
answer1==
No one
==
answer2==
Grant
==
answer3==
Grant's wife
==
answer4==
Grant's father
==
evaluator==

def evaluator(reponse):
    if reponse.sort() == ['Grant', "Grant's wife"]:
        return True, 'Bien joué'
    return False, 'Réponse incorrecte'

==
