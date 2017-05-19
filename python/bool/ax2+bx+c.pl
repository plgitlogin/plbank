# Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
author=Dominique Revuz 
name=ax2+bx+c.pl
title= Equation du second degrée 
tag=  # N'oubliez pas de remplir ce champs svp
template=/python/0PLG/template.pl
text==

# Equations du second degré

Le but de cet exercice est d’écrire un programme qui permet de déterminer le nombre de solutions réelles d’une équation du second degré de la forme ax2 + bx + c = 0 ou a, b et c sont des réels. Les cas suivants sont à considérer :
• si a=b=c=0,il y a une infinité de solutions;
	"Infinite de Solutions"
• si a=b=0 et c <> 0 , il n’y a pas de solution;
	"Pas de Solutions"
• si a=0 et b <> 0 et c <> 0 , il y a exactement une solution   x= -c/b ;
	"Exactement une solution"
• sinon, on calcule le discriminant ∆ = b2 − 4ac et,
	– si ∆<0, il n’y a pas de solution;
	"Pas de Solutions"
	– si ∆ = 0, il y a exactement une solution ;
	"Exactement une solution"
	– sinon ∆ > 0 et il y a exactement deux solutions
	"Exactement deux solutions".

1. Ecrire un programme qui demande à l’utilisateur de saisir au clavier les trois valeurs a, b et c et qui calcule et affiche le nombre de solutions réelles de l’équation du second degré associée.

==

# Choisir pltest ou soluce ou expectedoutput
resetcode=True
code==

R1 = "Infinite de Solutions."
R2 = "Pas de Solutions."
R3 = "Exactement une solution."
R4 = "Pas de Solutions."
R5 = "Exactement une solution."
R6 = "Exactement deux solutions."

a=int(input())
b=int(input())
c=int(input())

if ???? :
	print(R1)

==


input0=0 0 0
output0= "Infinite de Solutions."
feedback0="0*X**2+0*X+0=0 est vrai pour toutes les valeurs de X."
input1=0 0 1
output1= "Pas de Solutions."
feedback1="0*X**2+0*X+3=0 est fausse pour toutes les valeurs de X."
input2=0 1 -1
# x-1 = 0 
output2= "Exactement une solution."
feedback2=" Equation du premier degré"
input3=1 1 1
output3= "Pas de Solutions."
feedback3="pas de solutions réelles."
input4=1 2 1
output4= "Exactement une solution."
# (x+1)(x+1)=x2+2x+1
input5=1 -1 -2
output5= "Exactement deux solutions."
# (x+1)(x-2) X2-x-2
