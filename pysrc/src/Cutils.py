#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Cutils.py
#
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#

# Utils for the PL project C language


import pleval

def grade():
	x= pleval.pleval(dico=pleval.dicC)
	return x.grade()
