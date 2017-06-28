title==
MultipleGoodAnswers
==
answer1==
No one
==
answer2==
Grant
==
text==
What two people are entombed in Grant's tomb?
==
evaluator==

def evaluator(reponse):
    if reponse in ['Grant', "Grant's wife"]:
        return True, 'Bien joué'
    return False, 'Réponse incorrecte'

==
answer4==
Grant's father
==
answer3==
Grant's wife
==
type==
multiplechoices
==
name==
MultipleGoodAnswers
==
