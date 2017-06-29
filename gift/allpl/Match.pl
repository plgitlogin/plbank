answer2==
 dog food
==
text==
Which animal eats which food?
==
Question2==
dog 
==
answer1==
 cat food
==
title==
Match
==
Question1==
cat 
==
name==
Match
==
evaluator==

def evaluator(reponse):
    for rep_student in reponse :
        for rep in [' cat food', ' dog food']:
            if rep_student != rep:
                return False, "Mauvais matching"
            rep_exo.remove(0)
            continue
    return True, "Bien joué"

==
type==
matching
==
