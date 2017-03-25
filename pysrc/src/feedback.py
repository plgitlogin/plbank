#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  feedback.py
#  
#  Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
#  


"""
.. module:: feedback
   :platform: Unix, Windows
   :synopsis:Contruit le Html de Feedback pour un exercice PL.

.. moduleauthor:: Dominique Revuz <dr@univ-mlv.fr>

"""



from jinja2 import Template


def subnlbybr(str):
    """
>>> subnlbybr("\\n")
'<br/>'
    """
    return "<br/>".join(str.split("\n"))

class Feedback:
    """
	Classe de stockage et de production des sorties d'un exercie pl
    """
    def __init__(self):
        self.compilation = False # No error yet
        self.success = True
        self.showinput= True
        self.executionhistory = []
        self.feebacktext=""
        self.template = Template('''
<html><body>
<style>
    {%- if feedback.success %}
    h3 {color: powderblue;}
    div.feedback  {background-color:Chartreuse ;}
    {%- else %}
    h3 {color: red;}
    div.feedback  {color: pink;}
    div.feedback  {background-color: bleu;}
    {% endif %}
</style>
<div class="feedback">
{%- if  feedback.compile %}
    <h3> Erreur de Compilation</h3>{{- feedback.compilationError }}
{%- else %}
{% if feedback.asio %}
<h3> Executions </h3>
{%- for type,text in feedback.executionhistory %}
    {%- if feedback.showinput and type=="input" %}
    <span class="inputstyle">
        <p>{{text}}</p>
    </span>
    {%- endif %}
    {%- if type=="output" %}
    <span class="outputstyle">
        <p>Obtenu:<br/>{{text}}</p>
    </span>
    {%- elif type=="expected" %}
        <span class="outputstyle">
        <p>Attendu:<br/>{{text}}</p>
    </span>
    {%- endif %}
    {%- endfor %}
{%- else %}
<h3> Executions </h3>
{%- for type,text in feedback.executionhistory %}
    {%- if feedback.showinput and type=="input" %}
    <span class="inputstyle">
        <p>{{text}}</p>
    </span>
    {%- endif %}
    {%- if type=="output" %}
    <span class="outputstyle">
        <p><br/>{{text}}</p>
    </span>
    {%- endif %}
    {%- endfor %}
{%- endif %}
{%- endif %}
{%- if feedback.success %}
<H3> Bravo ! </H3>
{{ feedback.feedbacktext }}
{%- endif %}

</div>
<!-- feedback -->
</body></html>
''')

    def addInput(self,newinput):
        self.executionhistory.append(("input",subnlbybr(newinput)))
    def addOutput(self,newoutput):
        self.executionhistory.append(("output",subnlbybr(newoutput)))
    def addExpected(self,newoutput):
        self.executionhistory.append(("expected",subnlbybr(newoutput)))
    def addExpectedOptained(self,newoutput,expected):
        self.addExpected(expected)
        self.addOutput(newoutput)
        self.success=False
    def addCompilationError(self,text):
        self.compilationError=subnlbybr(text)
        self.compile = True
        self.success = False
    def addFeedback(self,text):
        self.feedbacktext = subnlbybr(text)
    def feedback(self):
        return self.template.render(feedback=self)
    def setsuccess(value):
        self.success = value

    def buildTemplate(self,newtemplatestring):
        self.template = Template(newtemplatestring)
        
