answer2==
Grant
==
text==
What two people are entombed in Grant's tomb?
==
answer4==
Grant's father
==
title==
MultipleGoodAnswers
==
answer1==
No one
==
name==
MultipleGoodAnswers
==
evaluator==

def evaluator(reponse):
    if reponse in ['Grant', "Grant's wife"]:
        return True, 'Bien joué'
    return False, 'Réponse incorrecte'

==
answer3==
Grant's wife
==
type==
multiplechoices
==
