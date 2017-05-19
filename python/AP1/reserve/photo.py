

import csv

def load(filename="data.csv"):
	firstcol="nomEntreprise"
	l=[]
	with open("data.csv","r") as csvfile :
		rows = csv.DictReader(csvfile)
		for row in rows:
			nome=row[firstcol]
			del row[firstcol]
			d[row[firstcol]].append(row)
	return l

def meilleur(region):
	l = load("data.csv")
	r=-1 # max
	for k in l.keys():
		d=l[k]
		if not region in d:
			return None
		if r < d[region]:
			resultat= [k]
		elif r == d[region]:
			resultat.append(k)
	return resultat


def rendement(region,surface):
	l = load("data.csv")
	r=-1 # max
	for d in l.values():
		if not region in d:
			return None
		if r < d[region]:
			resultat= d[region]*surface
	return resultat


def installation(region,surface):
	l = load("data.csv")
	r=-1 # max
	for k in l.keys():
			d=l[k]
			if not region in d:
					return None
			if r < d[region]:
					resultat= d[region]*surface
	return resultat
