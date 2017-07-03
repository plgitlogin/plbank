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
def evaluator(reponse, dic): 
    if reponse >= int(dic['mini']) and reponse <= int(dic['max']) :
        return True, 'Bonne réponse'
    return False, 'Réponse incorrecte'
==
