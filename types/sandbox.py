#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python [Version]
#
#  Author: Coumes Quentin     Mail: qcoumes@etud.u-pem.fr
#  Created: 2017-06-27
#  Last Modified: 2017-06-27


key_error = ['title',  'evaluator']
key_warning = ['text', 'author']

def check(dic):
    dic_key = dic.keys()
    warning = ""
        
    for key in key_error:
        if key not in dic_key:
            return False, "Error: Key missing in PL - '"+key+"'."
    
    if (not 'soluce' in dic_key) and (not 'testcode' in dic_key):
        return False, "Error: PL should contain at least one of the following key: 'soluce', 'testcode'"
    
    if ('basefiles' in dic and not 'plgrader.py' in dic['basefiles']) and (not 'grader' in dic_key):
        return False, "Error: Key missing in PL - 'grader'."
        
    for key in key_warning:
        if key not in dic_key:
            warning += "Warning: Key missing in PL - '"+key+"'.\n"
    
    if warning:
        return True, warning
    return True, None
        

