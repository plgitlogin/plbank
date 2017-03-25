import pytest
import plgrader
import json


def mysetup(student,pld):
    with open("student.py","w") as s:
        print(student,file=s)
    json.dump(pld,open("pl.json","w"))
    
testtemplate="""
{% if feedback.success %}success{% else %}echec{% endif %}
{%- if  feedback.compile %}{{ feedback.compilationError }}{%- else %}
{% if feedback.asio %}
{%- for type,text in feedback.executionhistory %}
{%- if feedback.showinput and type=="input" %}{{text}}{%- endif %}
{%- if type=="output" %}{{text}}
{%- elif type=="expected" %}
{{text}}{%- endif %}
{%- endfor %}
{%- else %}
{%- for type,text in feedback.executionhistory %}
{%- if feedback.showinput and type=="input" %}
{{text}}
{%- endif %}
{%- if type=="output" %}
{{text}}
{%- endif %}
{%- endfor %}
{%- endif %}
{%- endif %}
{%- if feedback.success %}{{ feedback.feedbacktext }}{%- endif %}
"""

import feedback

def test_feedback():
    f=feedback.Feedback()
    f.addFeedback("texte")
    print(f.feedback())
    assert f.feedback() == """
<html><body>
<style>
    h3 {color: powderblue;}
    div.feedback  {background-color:Chartreuse ;}
</style>
<div class="feedback">

<h3> Executions </h3>
<H3> Bravo ! </H3>
texte

</div>
<!-- feedback -->
</body></html>"""

def test_feedback2():
    f=feedback.Feedback()
    f.addCompilationError("beurk ca compile pas ")
    print(f.feedback())
    assert f.success == False
    assert f.feedback() == """
<html><body>
<style>
    h3 {color: red;}
    div.feedback  {color: pink;}
    div.feedback  {background-color: bleu;}
    
</style>
<div class="feedback">
    <h3> Erreur de Compilation</h3>beurk ca compile pas 

</div>
<!-- feedback -->
</body></html>"""


def test_plgrader_compile():
    mysetup(" print()\nsdlkjfhqkfjdshf",{})
    g= plgrader.Grader()
    g.fb.buildTemplate(testtemplate)
    x=json.loads(g.grade())
    assert x["success"]==False
    print(x["feedback"])
    assert x["feedback"] =="\nechecSorry: IndentationError: unexpected indent (student.py, line 1)"

def test_plgrader_good_expectedOutput():
    mysetup("print(1)\nprint(2)\n",{"expectedoutput":"1\n2\n"})
    g = plgrader.Grader()
    g.fb.buildTemplate(testtemplate)
    x = json.loads(g.grade())
    assert x["success"]==True
    print(x["feedback"])
    assert x["feedback"] =="""\nsuccess\n\n1<br/>2<br/>"""

def test_plgrader_no_grading_rules():
    mysetup("print(1)\nprint(2)\n",{"author":"LE roi de la bug"})
    g = plgrader.Grader()
    g.fb.buildTemplate(testtemplate)
    x = json.loads(g.grade())
    
    assert x["success"]==True
    print(x["feedback"])
    assert x["feedback"] == """\nsuccess\n<H1> Problème exercice mal défini </H1> Contacter l'auteur: LE roi de la bug<br/> Passez à l'exercice suivant."""



def test_plgrader_inputoutput_one():
    mysetup("print(input())\nprint(input())\n",{"author":"LE roi de la bug",
    "input0":"1\n2\n","output0":"1\n2\n"})
    g = plgrader.Grader()
    g.fb.buildTemplate(testtemplate)
    x = json.loads(g.grade())
    assert x["success"]==True
    print(x["feedback"])
    assert x["feedback"] == """"""

