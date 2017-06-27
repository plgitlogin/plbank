type==
direct
==
name==
SelectWithFeedback
==
title==
SelectWithFeedback
==
text==
What's between orange and green in the spectrum?
==
sandbox==
False
==
answer1==
yellow
==
answer2==
red
==
answer3==
blue
==
evaluator==

def evaluator(reponse): 
    for x in [('yellow', 'right; good!')]:
        if reponse[0] = x[0]:
            return True, x[1]
    for x in [('red', "wrong, it's yellow"), ('blue', "wrong, it's yellow")]:
        if reponse[0] =  x[0]:
            return False, x[1]

==
