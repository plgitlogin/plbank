title==
Match
==
answer1==
 cat food
==
answer2==
 dog food
==
text==
Which animal eats which food?
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
Question2==
dog 
==
Question1==
cat 
==
type==
matching
==
name==
Match
==
