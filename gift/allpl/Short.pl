answer2==
42
==
text==
Deep Thought said "
==
title==
Short
==
answer1==
forty two
==
name==
Short
==
evaluator==

def evaluator(reponse):
    for x in [('forty two', "Correct according to The Hitchhiker's Guide to the Galaxy!"), ('42', 'Correct, as told to Loonquawl and Phouchg'), ('forty-two', 'Correct!')]:
        if reponse == x[0]:
            return True, x[1]
    return False, 'Réponse incorrecte'

==
answer3==
forty-two
==
type==
short
==
