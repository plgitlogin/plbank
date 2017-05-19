
from itertools import groupby

def dohisto(l):
        l.sort()
        return groupby(l)


pltest="""
	>>> dohisto([1,2,1,2,1,2,4,5,6,8,19,1,2,2,1,2,4,5,6])
	>>>
	"""

	
data = [12.3,0.0,14.5,17.8,18,11.6,13.3,16.7,7,20,17,17,3]
from math import floor
def keyfunc(n):
	return floor(n/2)

for n in data:
	print(keyfunc(n),end=" ")

groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)
print(data)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)

for l in groups:
	print(l)
