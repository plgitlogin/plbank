type==
direct
==
name==
QQ5
==
title==
QQ5
==
text==
What is a number from 1 to 5?
==
sandbox==
False
==
evaluator==

def evaluator(reponse): 
    if reponse[0] in [1, 2, 3, 4, 5]:
        return True, 'Bonne réponse'
    return False, 'Réponse incorrecte'

==
