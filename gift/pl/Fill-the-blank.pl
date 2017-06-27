type==
direct
==
name==
Fill-the-blank
==
title==
Fill-the-blank
==
text==
Two plus
==
sandbox==
False
==
answer1==
two
==
answer2==
2
==
evaluator==

def evaluator(reponse):
    for x in [('two', ''), ('2', '')]:
        if reponse[0] = x[0]:
            return True, x[1]
    return False, 'Réponse incorrecte'

==
