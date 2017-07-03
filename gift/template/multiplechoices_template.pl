#  Author: Coumes Quentin     Mail: qcoumes@etud.u-pem.fr
#  Created: 2017-06-29
#  Last Modified: 2017-06-29


build==
def build(dic)
    n=1
    answer=list()
    while ('answer'+str(n) in pl_dic):
        answer.append(pl_dic['answer'+str(n)])
        n += 1
    dic['answer'] = answer
    return dic
==


form==
{% for item in answer %}
    <label class="radio-inline">
    <input type="radio" value="{{item}}" name="Answer">{{item}}
    </label>
{% endfor %}
==

evaluator==
def evaluator(reponse, dic): 
    if reponse in dic['right_answer']:
        for i in range(len(dic['answer'])):
            if reponse == dic['answer'][i]:
                return True, dic ['right_feedback'+str(i+1)]
            
    for i in range(len(dic['answer'])):
        if reponse == dic['answer'][i]:
            return False, dic['feedback'+str(i+1)]
    return False, ""
==
