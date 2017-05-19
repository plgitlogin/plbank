

import sys


patron="""
def test{{- Y }}(dd,gg):
	try:
		with open('{{- X}}',"r") as f:
			if not "0PLG" in f.read():
				print('{{- X}}',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','{{- X }}'])
				print('{{- X}}',file=gg)

	except:
		assert 0
	print('pas de '+'{{- X}}')
"""

import jinja2


print("import subprocess")
print("""import pytest

@pytest.fixture
def dd():
	f=open("/tmp/fixture.txt","a")
	yield f
	f.close()


@pytest.fixture
def gg():
        f=open("/tmp/valide.txt","a")
        yield f
        f.close()

""")


tampa = jinja2.Template(patron)
i=1
sys.argv.pop(0)
while sys.argv:
	yname = sys.argv[0].split("/")[-1]
	yname = yname.strip(".pl")
	print(tampa.render(X=sys.argv[0],Y=yname+str(i)))
	i = i + 1
	sys.argv.pop(0)

