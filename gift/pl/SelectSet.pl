type==
direct
==
name==
SelectSet
==
title==
SelectSet
==
text==
Who's buried in Grant's tomb?
==
sandbox==
False
==
answer1==
Grant
==
answer2==
no one
==
answer3==
Napoleon
==
answer4==
Churchill
==
answer5==
Mother Teresa
==
evaluator==

def evaluator(reponse): 
    for x in [('Grant', '')]:
        if reponse[0] = x[0]:
            return True, x[1]
    for x in [('no one', ''), ('Napoleon', ''), ('Churchill', ''), ('Mother Teresa', '')]:
        if reponse[0] =  x[0]:
            return False, x[1]

==
