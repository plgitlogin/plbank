answer2==
2
==
text==
Two plus
==
title==
Fill-the-blank
==
answer1==
two
==
name==
Fill-the-blank
==
evaluator==

def evaluator(reponse):
    for x in [('two', ''), ('2', '')]:
        if reponse == x[0]:
            return True, x[1]
    return False, 'Réponse incorrecte'

==
type==
short
==
