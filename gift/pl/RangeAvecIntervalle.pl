type==
direct
==
name==
RangeAvecIntervalle
==
title==
RangeAvecIntervalle
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
