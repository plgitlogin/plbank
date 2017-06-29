answer5==
Mother Teresa
==
answer2==
no one
==
text==
Who's buried in Grant's tomb?
==
answer4==
Churchill
==
title==
SelectSet
==
answer1==
Grant
==
name==
SelectSet
==
evaluator==

def evaluator(reponse): 
    if reponse == 'Grant':
        return True, 
    for x in [('no one', ''), ('Napoleon', ''), ('Churchill', ''), ('Mother Teresa', '')]:
        if reponse == x[0]:
            return False, x[1]

==
answer3==
Napoleon
==
type==
select
==
