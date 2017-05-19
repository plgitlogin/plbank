

import json
import hashlib

def addkeys(currentdict,d,key):
	for k in d.keys():
		currentdict[k].add(prefixe+":"+k)
		if isinstance(d[k], dict):
			addkeys(kset,d[k],prefixe+":"+k)
		else:

class Datas:
	def __init__(self,filename="view.json"):
		self.data = json.load(open("view.json","r"))
	def keys(self):
		""" 
		returns the set of keys used for elements of the exercices 
		"""
		topdic = dict()
		kset=set()
		filehashset = set()
		filenameset = set()
		stateset = set()
		maxf=0
		for d in self.data:# array 
			for k in d.keys(): # of dicts
				addkeys(topdic,d,k)

			if 'exercise' in d:
				if 'files' in d['exercise']:
					if maxf < len(d['exercise']['files']):
						maxf=len(d['exercise']['files'])
					for fd in d['exercise']['files']:
						filenameset.add(fd['name'])
						filenameset.add(fd['name'])
						hasher = hashlib.md5()
						hasher.update(fd['content'].encode('utf-8'))
						filehashset.add(hasher.hexdigest())
			if 'state' in d:
				if not d['state'] in stateset :
					print( d['state'])
					stateset.add( d['state'])
			else:
				print("no states")
		print("\n".join(sorted(kset)))
		print(maxf)
		print("\n".join(sorted(filenameset)))
		print(len(filenameset))
		print("\n".join(sorted(filehashset)))
		print(len(filehashset))
		return kset 


d = Datas().keys()

