def glork(n):
	print("X",end="") # pas de passage à la ligne écrit après le X
	return n>2

def blik(n):
	print("W",end="") 
	return n<1

n=3
if glork(n) or blik(n):
	n = n-3

if glork(n) and blik(n):
	n=n+2

if glork(n) or blik(n):
	n=0
