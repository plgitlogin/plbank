#  Author: Coumes Quentin     Mail: qcoumes@etud.u-pem.fr
#  Created: 2017-06-29
#  Last Modified: 2017-06-29


build==
n=1
answer=list()
while ('answer'+str(n) in pl_dic):
    answer.append(pl_dic['answer'+str(n)])
    n += 1
==


form==
{% for item in answer %}
    <label class="radio-inline">
    <input type="radio" value="{{item}}" name="Answer">{{item}}
    </label>
{% endfor %}
==
