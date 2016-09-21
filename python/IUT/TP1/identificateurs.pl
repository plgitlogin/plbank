# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=/python/IUT/TP1/identificateurs.pl
title=  Vérification des identificateurs 
tag= $identifier

text==

Eliminez les lignes ne contenant pas uniquement un identificateur utilisable pour une variable : 
	jenesuispasunidentifiant
	JeNeSuisPasUnIdentifiant
	Je ne suis pas un identifiant
	a
	a1
	1a
	abc
	def
	"bob"
	'bob'
	b*b
	__truc__
	@@Truc@@
	truc()
	$pip$
==

code==
jenesuispasunidentifiant
JeNeSuisPasUnIdentifiant
Je ne suis pas un identifiant
a
a1
1a
"bob"
bib
'bob'
b*b
__truc__
@@Truc@@
truc()
def
$pip$
==

grader= @ /python/IUT/TP1/drgrader.py
