#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  strangerecursivefunction.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  
# f(n)= f(n-1)+ f(n//f(n-1))  f(1)=3 f(0)=0 
# fournit le multiple de 3 strictement supérieur à n

def f(n):
	if n < 1 :
		return 0
	if n == 1:
		return 3
	fn1=f(n-1)
	return fn1+f(n//fn1)


for u in range(100):
	print(u,f(u) , ((u//3)+1)*3)

