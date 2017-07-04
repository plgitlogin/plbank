#  Author: Coumes Quentin     Mail: qcoumes@etud.u-pem.fr
#  Created: 2017-06-29
#  Last Modified: 2017-06-29

form==
<div class="input-group">
    <span class="input-group-addon">Réponse</span>
    <input id="msg" type="text" class="form-control" name="Answer" placeholder="">
</div>
==

evaluator==
def evaluator(response, dic):
    n = 1
    answer = list()
    while ('answer'+str(n) in dic):
        ans = dic['answer'+str(n)]
        if ('feedback'+str(n) in dic):
            fee = dic['feedback'+str(n)]
        else:
            fee = ('Bonne réponse')
        answer.append((ans, fee))
        n += 1
    for answer, feedback in answer:
        if response == answer:
            return True, feedback
    return False, 'Réponse incorrecte'
==
