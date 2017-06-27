type==
direct
==
name==
Q7
==
title==
Q7
==
text==
When was Ulysses S. Grant born?
==
sandbox==
False
==
evaluator==

def evaluator(reponse): 
    if reponse[0] in [1820, 1821, 1822, 1823, 1824]:
        return True, 'Bonne réponse'
    return False, 'Réponse incorrecte'

==
