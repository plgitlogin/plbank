template=@template.pl
title=Sac à lettres
text==
Écrivez une fonction //bag// qui retourne le sac des lettres d'une chaîne de caractère.
Il s'agit de retourner un dictionnaire qui associe à chaque lettre son nombre d'occurrences dans la chaîne.

Par exemple bag("abracadabra") devrait retourner le dictionnaire suivant :
{"a": 5, "b": 2, "c": 1, "d": 1, r": 2}

La fonction écrite devrait être généralisable pour toute séquence. Par exemple, on pourrait calculer bag((1,2,1,1,3)) qui retournerait :
{1: 3, 2: 1, 3: 1}
==
code==
import collections

@arguments("abracadabra", complexity=len("abracadabra"))
@arguments_generator(map(generator.random_string, range(0, 8) ))
def bag(x):
	b = collections.defaultdict(int)
	for e in x: b[e] += 1
	return b
==
testlist==[
	1,
	2,
	3]
==
testdict=={
	"element1":1,
	"element2":2,
	"element3":3
}
==
