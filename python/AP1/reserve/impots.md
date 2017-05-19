

 

# Barème 2017 de l'impôt sur le revenu

Calcul hors niches fiscales ...

RI Revenu imposable

N Nombre de parts

R=RI/N

|Tranche du revenu net imposable R|Taux marginal d'imposition|Formule de calcul de l'impôt brut|
|---------------------------------|--------------------------|---------------------------------|
|Jusqu'à 9 710 |0% |-|
|De 9 710 à 26 818 |14% |(RI x 0,14) - (1359,40 x N)|
|De 26 818 à 71 898 |30% |(RI x 0,3) - (5650,28 x N)|
|De 71 898 à 152 260 |41% |(RI x 0,41) - (13 559,06 x N)|
|Plus de 152 260 |45% |(RI x 0,45) - (19 649,46 x N)|

Utilisez les constantes :


	l1 = [9710,26818,71898,152260]
	l2 = [0,14,30,41,45]
	l3 = [0,1359.4,5650.28,13559.06,19649.46]


**Ecrire une fonction _calcul(RI,N)_ qui retourne le montant de l'impot à acquiter pour une famille avec N part qui ont R de revenu global.**

**Ecrire une fonction _tauxglobal(RI,N)_ qui retourne le taux global I/RI d'imposition . ** 

**Ecrire une fonction _exemples(EX)_ qui affiche pour chaque couple de valeur (RI,N) de la liste _EX_ la ligne suivante :**

Pour
	EX=[(12000,1),(120000,5)]
	_exemples(EX)_ affiche


	Pour un revenu imposable de 12000 et 1 part(s) l'import est de 321 € et le taux global de 3 %.
	Pour un revenu imposable de 12000 et 5 part(s) l'import est de 321 € et le taux global de 3 %.

