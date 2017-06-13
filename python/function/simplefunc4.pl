template=/python/0PLG/template.pl
title=Simple 3 
name= Une fonction 

tag=list|function|dict
text==

# Histogramme de caractères

Note: **Si vous avez besoin des fonctions que vous avez écritent de l'exercice précédent vous pouvez revenir en arrière et récupérer le code.**

Ecrire une fonction **histo** qui prend une **chaine** en parametres et qui affiche pour chaque lettre apparaisant dans la **chaine** le nombre de fois ou elle apparait:

	histo("Abracadabra")
	A 1
	a 4
	b 2
	c 1
	d 1
	r 2

Ecrire une fonction **toupper** qui prend un caractère et le retourne sauf si il est entre 'a' et 'z' dans ce cas il retourne le caractère 'A' à 'Z'  correspondant.

	toupper('%')
	%
	toupper('e')
	'E'
	toupper('Z')
	'Z'


Ecrire une fonction **histo2** qui prend une **chaine** en parametres et qui affiche pour chaque lettre apparaisant dans la **chaine** le nombre de fois ou elle apparait sans faire de différence entre minuscules et majuscules :


	histo2("Abracadabra")
	A 5
	B 2
	C 1
	D 1
	R 2


==


pltest==
>>> toupper("abracadabra")
'ABRACADABRA'
>>> histo("abracadabra")
a 5
b 2
c 1
d 1
r 2
>>> histo("Abracadabra")
A 1
a 4
b 2
c 1
d 1
r 2
>>> histo("AbracadabraZ")
A 1
Z 1
a 4
b 2
c 1
d 1
r 2
>>> histo2("AbracadabraZ")
A 5
B 2
C 1
D 1
R 2
Z 1
>>> 
==

soluce==
def toupper(c):
	if 'a'<= c <= 'z':
		return chr(ord(c)-(97-65))
	else:
		return c


def histo(s):
	d={}
	for l in s:
		if l in d:
			continue
		d[l]=0
		for v in s:
			if l==v:
				d[l]+=1
	for k in sorted(d.keys()):
		print(k,d[k])

def histo2(s):
	d={}
	for l in s:
		l = toupper(l)
		if l in d:
			continue
		d[l]=0
		for v in s:
			v = toupper(v)
			if l==v:
				d[l]+=1
	for k in sorted(d.keys()):
		print(k,d[k])



==


