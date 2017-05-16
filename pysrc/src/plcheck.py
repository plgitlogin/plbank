

import subprocess
import sys
import pathlib
from .question import Question
from .plrequest import SandboxSession
import json

debug=True
verbose=False

def checkpltpfile(repo_dir,exopath,sandboxurl="http://127.0.0.1:8000/sandbox/?action=execute"):
	pe = pathlib.Path(exopath)
	s = str(pe.resolve())
	if verbose:
		print("Test de "+s+"\nsur : "+sandboxurl)
	q=question.Question(s[len(str(repo_dir)):],root=repo_dir)
	dico = q.dico
	for key in ["introduction","concept","name"]:
		if not key in dico:
			raise question.ErrorPL("PLTP sans balise "+key)
	if verbose: print(dico['concept'])

	### FIX ME tester si les fichier sont connus de git et a jour

def main(repo_dir,exopath,sandboxurl="http://127.0.0.1:8000/sandbox/?action=execute"):
	if exopath.endswith(".pl"):
		return checkplfile(repo_dir,exopath,sandboxurl=sandboxurl)
	elif exopath.endswith(".pltp"):
		return checkpltpfile(repo_dir,exopath,sandboxurl=sandboxurl)

def checkplfile(repo_dir,exopath,sandboxurl="http://pl-sandbox-test.u-pem.fr/?action=execute",studentfile="print(3000)"):
	pe = pathlib.Path(exopath)
	s = str(pe.resolve())
	if verbose : print("Test de "+s+"\nsur : "+sandboxurl)
	q=question.Question(s[len(str(repo_dir)):],root=repo_dir)
	if verbose : print("Question chargée") 
	if "testcode" in q.dico:
		studentfile=q.dico["testcode"]
	elif "soluce" in q.dico :
		studentfile=q.dico["soluce"]
	s= plrequest.SanboxSession(q,sandboxurl,studentfile)# question,url,studentfile
	result = json.loads(s.answer.text)
	assert result["platform_error"] == []
	#print(result)
	if verbose: print("La correction pour "+studentfile+" est "+result["grade"]['feedback'])
	with open("/tmp/result.html","w")as rf:
		print(result["grade"]['feedback'],file=rf)
	print("le feedback est dans file:///tmp/result.html ")
	return s.answer.text

def getrepodir():
	return subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).communicate()[0].rstrip().decode("utf-8")

def docommit(name):
	subprocess.run(['git', 'commit','-m','"plcheck commit"', name])


if __name__ == '__main__':

	repo_dir = getrepodir()
	if repo_dir == "" :
		sys.exit(-1)

	if debug :
		print("Traitement du repo"+repo_dir)

	sys.argv.pop(0)
	while sys.argv[0][0]=='-':
		if sys.argv[0][1]=='v':
			verbose = True
		sys.argv.pop(0)
	while sys.argv :
		try:
			main(repo_dir,sys.argv[0])
			docommit(sys.argv[0])
		except question.ErrorPL as e:
			print("Fichier ",sys.argv[0]," incorrect ",str(e))
		except Exception as e:
			print("Problem avec ",sys.argv[0])
			raise e
		sys.argv.pop(0)
		if sys.argv :
			input("Fichier suivant")

	sys.exit(0)
