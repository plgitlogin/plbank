
# Rendement énergetique 
Le rendement des panneaux solaires photovoltaïques  (panneaux
qui produisent de l’électricité grâce au soleil) dépend du type de panneaux, de la surface des panneaux et du niveau d’ensoleillement reçu. Il est mesuré en kilowatts-heure par mètre carré, soit 
$$kWh / m²$$.
Une 
production annuelle de $$100 kWh / m²$$ indique donc que $$1 m²$$ de panneaux produit $$100 kWh$$.     
Le tableau suivant présente les rendements annuels en $$kWh / m²$$ de panneaux solaires 
produits par 3 sociétés en fonction de la région d’installation.
Panneau EKL-R | Panneau DeLux Power | Panneau RA-élec
-|:-:|:-:|:-:|
Nord|110|115|113
Gironde|140|135|148
Corse|185|175|180

On suppose que le fichier de donnée "data.csv" est de la forme :

	nomEntreprise,Nord,Gironde,Corse,autresregions
	Panneau EKL-R,110,140,185,etc
	Panneau DeLux Power,115,135,175,etc
	Panneau RA-élec,113,148,180,etc

## Partie 1
Ecrire une fonction **load(filename)**  qui charge le fichier filename="data.csv" pour créer une liste de dictionnaires avec comme clef le nom de l'entreprise, et pour les clefs  du sous dictionnaire les noms de region de la première ligne du fichier ce qui donne ceci avec les données précédentes (ordre aléatoire des clefs):

	[{'Gironde': '140', 'Nord': '110', 'Corse': '185', 'autresregions': 'etc', 'nomEntreprise': 'Panneau EKL-R'}, {'Gironde': '135', 'Nord': '115', 'Corse': '175', 'autresregions': 'etc', 'nomEntreprise': 'Panneau DeLux Power'}, {'Gironde': '148', 'Nord': '113', 'Corse': '180', 'autresregions': 'etc', 'nomEntreprise': 'Panneau RA-élec'}]

Cette struture de donnée s'utilise dans le code suivant:

	for dico in load("data.csv"):
		if dico['nomEntreprise'] == 'Panneau DeLux Power':
			print("Pour la corse ",dico['Corse'])

affiche

	Pour la corse 175

## Partie 2
Pour aider M. P HINEAS, qui habite en Gironde, qui souhaite installer 15 m² de panneaux. Ecrire une fonction _meilleur("Gironde")_ qui retourne None si la région n'existe pas et sinon retoure une liste d'entreprise ayant les meilleurs rendements. Et une fonction rendement qui prend en parametre une région, une surface et retourne le meilleur rendement annuel de cette surface dans cette région. 

	>>> meilleur("Gironde")
	["Panneau RA-élec"]
	>>> meilleur("Corse")
	["Panneau EKL-R"]
	>>> meilleur("Alsace")
	None 
	>>> rendement("Gironde",15)
	2220
	

## Partie 3
Pour aider M. F ERB, qui habite en corse et qui souhaite savoir qu'elle marque installer et combien il faut en installer pour optenir un rendement minumum annuel de 5180 KWh

	>>> installation("Corse",5180)
	["Panneau EKL-R",28.0]
	>>> installation("Gironde",5180)
	["Panneau RA-élec",35.0]

==


testcode=@photo.py
