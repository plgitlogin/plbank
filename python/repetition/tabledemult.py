#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabledemult.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  

def line(x):
		print(" %d " % x, end="|" )
		for i in range(1,11):
			if i*x<10:
				print(" ",end="")
			print(i*x, end="|")

print(" \ | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|")
print("   ", end="+" )
for i in range(1,11):
	print("  +",end="")
print()
for i in range(1,10):
	line(i)
	print()

