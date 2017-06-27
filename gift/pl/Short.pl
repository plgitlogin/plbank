type==
direct
==
name==
Short
==
title==
Short
==
text==
Deep Thought said "
==
sandbox==
False
==
answer1==
forty two
==
answer2==
42
==
answer3==
forty-two
==
evaluator==

def evaluator(reponse):
    for x in [('forty two', "Correct according to The Hitchhiker's Guide to the Galaxy!"), ('42', 'Correct, as told to Loonquawl and Phouchg'), ('forty-two', 'Correct!')]:
        if reponse[0] = x[0]:
            return True, x[1]
    return False, 'Réponse incorrecte'

==
