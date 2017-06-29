title==
SelectSet
==
answer1==
Grant
==
answer2==
no one
==
text==
Who's buried in Grant's tomb?
==
answer5==
Mother Teresa
==
answer4==
Churchill
==
answer3==
Napoleon
==
evaluator==

def evaluator(reponse): 
    if reponse == 'Grant':
        return True, 
    for x in [('no one', ''), ('Napoleon', ''), ('Churchill', ''), ('Mother Teresa', '')]:
        if reponse == x[0]:
            return False, x[1]

==
type==
select
==
name==
SelectSet
==
