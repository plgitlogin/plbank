# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name= Quelques Constantes
title=   # N'oubliez pas de remplir ce champs svp
tag=  # N'oubliez pas de remplir ce champs svp
template=/python/exemple/autogradertemplate
text==


Sachant que l'unité de distance la plus petite est 
$$ 1,616199 10^{−35}$$ metres soit la Longueur de Planck
et que $$1,3 10^{28}$$ metres distance du plus loingtain quasar.  

Dans un interpréteur python essayez le code suivant :


	PI=3.14156 # en americain  
	km= 10**3 # un kilometre c'est 1000 metres
	a=1 000 000 000 # erreur de syntaxe
	a=1.000.000.000 # erreur de syntaxe
	a=1,000,000,000 # 4 valeurs !!!!
	a
	a=10^9 
	a # surprise 
	a=10**9
	a


Puis répondez à l'exercice en calculant la distance de ce quasar en longueurs de Planck et en affichant celle ci la sur une ligne en notation mathématique (affichage par défaut). Puis sous forme d'un entier en utilisant:

	print(int(ladistance))


==

expectedoutput==
8.04356394231156e+62
804356394231156020197466798869532453036311623701109748489256960
==



