title==
RangeAvecTolerance
==
text==
What is a number from 1 to 5?
==
evaluator==

def evaluator(reponse): 
    if reponse >= 1 and reponse <= 5 :
        return True, 'Bonne réponse'
    return False, 'Réponse incorrecte'

==
type==
numeric
==
name==
RangeAvecTolerance
==
