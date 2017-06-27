type==
direct
==
name==
Match
==
title==
Match
==
text==
Which animal eats which food?
==
sandbox==
False
==
answer1==
 cat food
==
answer2==
 dog food
==
Question1==
cat 
==
Question2==
dog 
==
evaluator==

def evaluator(reponse):
    rep_exo = [' cat food', ' dog food']
    for rep_student in reponse :
        for rep in rep_exo:
            if rep_student != rep:
                return False, "Mauvais matching"
            rep_exo.remove(0)
            continue
    return True, "Bien joué"
    

==
