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


import plrequest
import question


class SanboxSession:
	def __init__(self,question,url):
		self.question = question
		self.url = url

	def createEnvFile(self):
		from shutil import rmtree
		rmtree('/tmp/env/')
		p=Path('/tmp/env/')
		p.mkdir()
		for name,



	def call(self,studentfile):
		self.files = {'environment': open('/tmp/env.zip', 'rb'),'student.py':studentfile}
		self.answer = requests.post(self.url,data=self.question.dico,files=self.files,timeout=0.1)




