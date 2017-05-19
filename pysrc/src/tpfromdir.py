#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fromdir.py
#  
#  Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
#  
#  output a pltp file from a list of paths

from jinja2 import Template


tinta="""
author={{author}}
name=auto_exo
{%- if tag %}
tag={{tag}}
{%- endif %}
introduction==
{{ intro }}
==
concept==NONE
{{li }}
==
"""

def main(argv):
    if argv :
        d={"tag":"all","author":"Dominique Revuz","intro":"Tout les exos de la plateforme ","li":"@ "+"\n@ ".join(argv)}
        thetemplate = Template(tinta)
        return thetemplate.render(d)
    else:
        print("pas d'arguments ",file=sys.stderr)

if __name__ == '__main__':
    import sys
    sys.argv.pop(0) # remove first argument name of script 
    s = main(sys.argv)
    print(s)
