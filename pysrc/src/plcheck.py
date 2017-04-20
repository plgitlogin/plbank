

import subprocess
import sys
import pathlib
import question
import plrequest
import json

debug=False

def main(repo_dir,exopath,sandboxurl="http://pl-sandbox-test.u-pem.fr/?action=execute",studentfile="print(3000)"):
	
	pe = pathlib.Path(exopath)
	s = str(pe.resolve())
	print("Test de "+s)
	q=question.Question(s[len(str(repo_dir)):],root=repo_dir)
	if "testcode" in q.dico:
		studentfile=q.dico["testcode"]
	elif "soluce" in q.dico :
		studentfile=q.dico["soluce"]
	s= plrequest.SanboxSession(q,sandboxurl,studentfile)
	result = json.loads(s.answer.text)
	
	assert result["platform_error"] == []
	#print("La correction pour "+studentfile+" est "+result["grade"]['feedback'])
	with open("/tmp/result.html","w")as rf:
		print(result["grade"]['feedback'],file=rf)
	print("le feedback est dans file:///tmp/result.html ")
	return s.answer.text

def getrepodir():
	return subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).communicate()[0].rstrip().decode("utf-8")


if __name__ == '__main__':
	repo_dir = getrepodir()
	if repo_dir == "" :
		sys.exit(-1)

	if debug :
		print("Traitement du repo"+repo_dir)

	sys.argv.pop(0)
	while sys.argv :
		main(repo_dir,sys.argv[0])
		sys.argv.pop(0)
	sys.exit(0)
