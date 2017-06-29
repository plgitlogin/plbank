title==
MultipleNumeric
==
text==
When was Ulysses S. Grant born?
==
evaluator==

def evaluator(reponse): 
    if reponse >= 1820 and reponse <= 1824 :
        return True, 'Bonne réponse'
    return False, 'Réponse incorrecte'

==
type==
numeric
==
name==
MultipleNumeric
==
