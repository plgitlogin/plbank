#  Author: Coumes Quentin     Mail: qcoumes@etud.u-pem.fr
#  Created: 2017-06-29
#  Last Modified: 2017-06-29


form==
<label class="checkbox-inline">
    <input type="radio" value="True" name="Answer">Vrai
</label>
<label class="radio-inline">
    <input type="radio" value="False" name="Answer">Faux
</label>
==


evaluator==
def evaluator(reponse, dic):
    if (str(dic['answer']) == reponse):
        return True, str(dic['feedback_correct'])
    return False, str(dic['feedback_wrong'])
==
