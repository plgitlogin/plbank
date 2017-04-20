#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  request.py
#  
#  Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
#  

__doc__ = """

	Ce fichier a pour objectif de gérer les comunications
	avec la sandbox.
	"""


import requests
import question


class SanboxSession:
	def __init__(self,question,url):
		self.question = question
		self.url = url

	def call(self,timeout=0):
		self.answer = requests.post(self.url,data=self.question.dico,timeout=timeout)




