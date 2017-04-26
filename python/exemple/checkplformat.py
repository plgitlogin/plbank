#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  homemadeplparse.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import re
from collections import defaultdict






def getdico( strng ):
	n=0
	dico=defaultdict()
	state = 0 # start of parsing
	we =  re.compile("[^=\\n]+")
	with open(strng,"r") as iniFile :
		for line in  iniFile.readlines():
			n+=1; print("%d %s" % (n,line))
			if state == 0:
				debut = line.split("#")[0]
				m = we.match(debut)
				if m == None:
					continue
				key = m.group()
				print("$$$ %s $$$" % (key))
				if debut[m.end()] != '=':
					continue
				if debut[m.end()+1] != '=':
					value = debut[m.end()+1:]
					value = value.strip('\n')
					dico[key]=value
				else:# la fin d'une ligne de la forme mot==blabla est un commentaire
					state =1
					value = ""
			elif state== 1: # nous sommes dans un champs multiligne
				if line.startswith("==") :
					dico[key]=value
					state = 0
				else:
					value += line
					
	tokens=dico
	return tokens
    
def dumppljson(filename):
	Xini = getdico(filename)
	ini=dict()
	ini.update(Xini)
	v0 = ["title","text","grader"] # obligatoire 
	v1 = ["title","text","files","code","grader","author","template","soluce","version"] # version 1 
	v2 = ["difficulty","echec","hint","hint0","hint1","hint2","hint3","input","taboo","timeout","inputgenerator",""] # version 2
	v3 = [ "nimportequoi" ] # euh ...

	for k in v0:
		if ini[k] == None :
			print("Erreur la primitive %s est obligatoire " % (k))	

	for k in ini.keys():
		if not k in v1:
			if k in v2:
				print("Warning la primitive %s est version 2 " % (k))
			else:
				print("Erreur la primitive %s n'est pas reconnue" % (k))

	print(ini)

	import json
	json.dump(ini,open("pl.json","w"))


if __name__ == '__main__':
	import sys
	if len(sys.argv) >0 and sys.argv[1].endswith(".pl") :
		sys.exit(dumppljson(sys.argv[1]))

