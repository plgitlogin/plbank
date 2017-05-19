#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  calculimpots.py
#  
#  Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>
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

def calcul(R,N):
	"""
	>>> calcul(0,5)
	0
	>>> calcul(12000,1)
	321
	>>> calcul(1200000,4)
	461402
	
	"""
	
	l1 = [9710,26818,71898,152260]
	l2 = [0,14,30,41,45]
	l3 = [0,1359.4,5650.28,13559.06,19649.46]
	if N <1:
		N=1
	RP=R/N
	i =0 
	while i<len(l1) and RP >l1[i]:
		i+=1
	return round(R*l2[i]/100-N*l3[i])


def tauxglobal(RI,N):
	return round(calcul(RI,N)/RI*100)


def exemples(EX):
	"""
	>>> exemples([(8899,1)])
	Pour un revenu imposable de 8899 et 1 part(s) l'import est de 0 € et le taux global de 0 %.
	>>> exemples([(88909,1)])
	Pour un revenu imposable de 88909 et 1 part(s) l'import est de 22894 € et le taux global de 26 %.
	>>> exemples([(88909,1),(56789,2.5)])
	Pour un revenu imposable de 88909 et 1 part(s) l'import est de 22894 € et le taux global de 26 %.
	Pour un revenu imposable de 56789 et 2.5 part(s) l'import est de 4552 € et le taux global de 8 %.
	>>> exemples([(88909,1),(78000,2.5)])
	Pour un revenu imposable de 88909 et 1 part(s) l'import est de 22894 € et le taux global de 26 %.
	"""
	for r,n in EX:
		print("Pour un revenu imposable de {} et {} part(s) l'import est de {} € et le taux global de {} %.".format(r,n,calcul(r,n),tauxglobal(r,n)))



def main(args):
	R = input("votre Revenu a l'euro près ?")
	R = int(R)
	N = int(input("Nombre de Part ?"))
	print(" Vous devrez vous acquitez d'un impot de ",calcul(R,N)," euros")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
