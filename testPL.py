import subprocess
import pytest

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



def testempty1(dd,gg):
	try:
		with open('python/0PLG/TPE/empty.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/0PLG/TPE/empty.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/0PLG/TPE/empty.pl'])
				print('python/0PLG/TPE/empty.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/0PLG/TPE/empty.pl')

def testerror2(dd,gg):
	try:
		with open('python/0PLG/TPE/error.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/0PLG/TPE/error.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/0PLG/TPE/error.pl'])
				print('python/0PLG/TPE/error.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/0PLG/TPE/error.pl')

def testfunction0013(dd,gg):
	try:
		with open('python/0PLG/TPE/function001.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/0PLG/TPE/function001.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/0PLG/TPE/function001.pl'])
				print('python/0PLG/TPE/function001.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/0PLG/TPE/function001.pl')

def testidentificateurs4(dd,gg):
	try:
		with open('python/0PLG/TPE/identificateurs.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/0PLG/TPE/identificateurs.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/0PLG/TPE/identificateurs.pl'])
				print('python/0PLG/TPE/identificateurs.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/0PLG/TPE/identificateurs.pl')

def testoperator0015(dd,gg):
	try:
		with open('python/0PLG/TPE/operator001.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/0PLG/TPE/operator001.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/0PLG/TPE/operator001.pl'])
				print('python/0PLG/TPE/operator001.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/0PLG/TPE/operator001.pl')

def testoperatorModulo6(dd,gg):
	try:
		with open('python/0PLG/TPE/operatorModulo.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/0PLG/TPE/operatorModulo.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/0PLG/TPE/operatorModulo.pl'])
				print('python/0PLG/TPE/operatorModulo.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/0PLG/TPE/operatorModulo.pl')

def testvariableAkiki7(dd,gg):
	try:
		with open('python/0PLG/TPE/variableAkiki.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/0PLG/TPE/variableAkiki.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/0PLG/TPE/variableAkiki.pl'])
				print('python/0PLG/TPE/variableAkiki.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/0PLG/TPE/variableAkiki.pl')

def testtemplate8(dd,gg):
	try:
		with open('python/0PLG/template.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/0PLG/template.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/0PLG/template.pl'])
				print('python/0PLG/template.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/0PLG/template.pl')

def testcorrigemoi_19(dd,gg):
	try:
		with open('python/AP1/TP1/corrigemoi_1.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/AP1/TP1/corrigemoi_1.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/AP1/TP1/corrigemoi_1.pl'])
				print('python/AP1/TP1/corrigemoi_1.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/AP1/TP1/corrigemoi_1.pl')

def testcorrigemoi_210(dd,gg):
	try:
		with open('python/AP1/TP1/corrigemoi_2.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/AP1/TP1/corrigemoi_2.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/AP1/TP1/corrigemoi_2.pl'])
				print('python/AP1/TP1/corrigemoi_2.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/AP1/TP1/corrigemoi_2.pl')

def testcorrigemoi_311(dd,gg):
	try:
		with open('python/AP1/TP1/corrigemoi_3.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/AP1/TP1/corrigemoi_3.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/AP1/TP1/corrigemoi_3.pl'])
				print('python/AP1/TP1/corrigemoi_3.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/AP1/TP1/corrigemoi_3.pl')

def testcorrigemoi_412(dd,gg):
	try:
		with open('python/AP1/TP1/corrigemoi_4.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/AP1/TP1/corrigemoi_4.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/AP1/TP1/corrigemoi_4.pl'])
				print('python/AP1/TP1/corrigemoi_4.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/AP1/TP1/corrigemoi_4.pl')

def testcorrigemoi_513(dd,gg):
	try:
		with open('python/AP1/TP1/corrigemoi_5.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/AP1/TP1/corrigemoi_5.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/AP1/TP1/corrigemoi_5.pl'])
				print('python/AP1/TP1/corrigemoi_5.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/AP1/TP1/corrigemoi_5.pl')

def testcorrigemoi_614(dd,gg):
	try:
		with open('python/AP1/TP1/corrigemoi_6.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/AP1/TP1/corrigemoi_6.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/AP1/TP1/corrigemoi_6.pl'])
				print('python/AP1/TP1/corrigemoi_6.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/AP1/TP1/corrigemoi_6.pl')

def testcorrigemoi_715(dd,gg):
	try:
		with open('python/AP1/TP1/corrigemoi_7.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/AP1/TP1/corrigemoi_7.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/AP1/TP1/corrigemoi_7.pl'])
				print('python/AP1/TP1/corrigemoi_7.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/AP1/TP1/corrigemoi_7.pl')

def testconstantestypes16(dd,gg):
	try:
		with open('python/IUT/TP1/constantestypes.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/constantestypes.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/constantestypes.pl'])
				print('python/IUT/TP1/constantestypes.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/constantestypes.pl')

def testerror17(dd,gg):
	try:
		with open('python/IUT/TP1/error.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/error.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/error.pl'])
				print('python/IUT/TP1/error.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/error.pl')

def testerrorindent18(dd,gg):
	try:
		with open('python/IUT/TP1/errorindent.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/errorindent.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/errorindent.pl'])
				print('python/IUT/TP1/errorindent.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/errorindent.pl')

def testerrorsyntax19(dd,gg):
	try:
		with open('python/IUT/TP1/errorsyntax.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/errorsyntax.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/errorsyntax.pl'])
				print('python/IUT/TP1/errorsyntax.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/errorsyntax.pl')

def testerrortype20(dd,gg):
	try:
		with open('python/IUT/TP1/errortype.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/errortype.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/errortype.pl'])
				print('python/IUT/TP1/errortype.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/errortype.pl')

def testidentificateurs21(dd,gg):
	try:
		with open('python/IUT/TP1/identificateurs.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/identificateurs.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/identificateurs.pl'])
				print('python/IUT/TP1/identificateurs.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/identificateurs.pl')

def testififif22(dd,gg):
	try:
		with open('python/IUT/TP1/ififif.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/ififif.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/ififif.pl'])
				print('python/IUT/TP1/ififif.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/ififif.pl')

def testoperator00123(dd,gg):
	try:
		with open('python/IUT/TP1/operator001.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/operator001.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/operator001.pl'])
				print('python/IUT/TP1/operator001.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/operator001.pl')

def testoperator00224(dd,gg):
	try:
		with open('python/IUT/TP1/operator002.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/operator002.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/operator002.pl'])
				print('python/IUT/TP1/operator002.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/operator002.pl')

def testoperator00325(dd,gg):
	try:
		with open('python/IUT/TP1/operator003.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/operator003.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/operator003.pl'])
				print('python/IUT/TP1/operator003.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/operator003.pl')

def testrintbonjour26(dd,gg):
	try:
		with open('python/IUT/TP1/printbonjour.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/printbonjour.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/printbonjour.pl'])
				print('python/IUT/TP1/printbonjour.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/printbonjour.pl')

def testrintinput27(dd,gg):
	try:
		with open('python/IUT/TP1/printinput.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/printinput.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/printinput.pl'])
				print('python/IUT/TP1/printinput.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/printinput.pl')

def testvariabletypes28(dd,gg):
	try:
		with open('python/IUT/TP1/variabletypes.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/TP1/variabletypes.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/TP1/variabletypes.pl'])
				print('python/IUT/TP1/variabletypes.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/TP1/variabletypes.pl')

def testtemplate29(dd,gg):
	try:
		with open('python/IUT/template.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/IUT/template.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/IUT/template.pl'])
				print('python/IUT/template.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/IUT/template.pl')

def testnuitsdamour30(dd,gg):
	try:
		with open('python/TP1/nuitsdamour.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/TP1/nuitsdamour.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/TP1/nuitsdamour.pl'])
				print('python/TP1/nuitsdamour.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/TP1/nuitsdamour.pl')

def testvaleurs31(dd,gg):
	try:
		with open('python/TP1/valeurs.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/TP1/valeurs.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/TP1/valeurs.pl'])
				print('python/TP1/valeurs.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/TP1/valeurs.pl')

def testbonlcond32(dd,gg):
	try:
		with open('python/bool/bonlcond.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/bool/bonlcond.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/bool/bonlcond.pl'])
				print('python/bool/bonlcond.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/bool/bonlcond.pl')

def testsisi0133(dd,gg):
	try:
		with open('python/bool/sisi01.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/bool/sisi01.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/bool/sisi01.pl'])
				print('python/bool/sisi01.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/bool/sisi01.pl')

def testsisi0234(dd,gg):
	try:
		with open('python/bool/sisi02.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/bool/sisi02.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/bool/sisi02.pl'])
				print('python/bool/sisi02.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/bool/sisi02.pl')

def testsisi0335(dd,gg):
	try:
		with open('python/bool/sisi03.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/bool/sisi03.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/bool/sisi03.pl'])
				print('python/bool/sisi03.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/bool/sisi03.pl')

def testsisi0436(dd,gg):
	try:
		with open('python/bool/sisi04.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/bool/sisi04.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/bool/sisi04.pl'])
				print('python/bool/sisi04.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/bool/sisi04.pl')

def testtridetrois37(dd,gg):
	try:
		with open('python/bool/tridetrois.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/bool/tridetrois.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/bool/tridetrois.pl'])
				print('python/bool/tridetrois.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/bool/tridetrois.pl')

def teststr_and_int38(dd,gg):
	try:
		with open('python/conversion/str_and_int.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/conversion/str_and_int.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/conversion/str_and_int.pl'])
				print('python/conversion/str_and_int.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/conversion/str_and_int.pl')

def testdirect39(dd,gg):
	try:
		with open('python/dynamic/direct.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/direct.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/direct.pl'])
				print('python/dynamic/direct.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/direct.pl')

def testdyna140(dd,gg):
	try:
		with open('python/dynamic/dyna1.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna1.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna1.pl'])
				print('python/dynamic/dyna1.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna1.pl')

def testdyna241(dd,gg):
	try:
		with open('python/dynamic/dyna2.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna2.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna2.pl'])
				print('python/dynamic/dyna2.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna2.pl')

def testdyna342(dd,gg):
	try:
		with open('python/dynamic/dyna3.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna3.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna3.pl'])
				print('python/dynamic/dyna3.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna3.pl')

def testdyna443(dd,gg):
	try:
		with open('python/dynamic/dyna4.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna4.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna4.pl'])
				print('python/dynamic/dyna4.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna4.pl')

def testdyna544(dd,gg):
	try:
		with open('python/dynamic/dyna5.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna5.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna5.pl'])
				print('python/dynamic/dyna5.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna5.pl')

def testdyna645(dd,gg):
	try:
		with open('python/dynamic/dyna6.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna6.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna6.pl'])
				print('python/dynamic/dyna6.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna6.pl')

def testdyna746(dd,gg):
	try:
		with open('python/dynamic/dyna7.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna7.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna7.pl'])
				print('python/dynamic/dyna7.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna7.pl')

def testdyna847(dd,gg):
	try:
		with open('python/dynamic/dyna8.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna8.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna8.pl'])
				print('python/dynamic/dyna8.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna8.pl')

def testdyna948(dd,gg):
	try:
		with open('python/dynamic/dyna9.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/dynamic/dyna9.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/dynamic/dyna9.pl'])
				print('python/dynamic/dyna9.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/dynamic/dyna9.pl')

def testvariadic49(dd,gg):
	try:
		with open('python/exemple/variadic.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/exemple/variadic.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/exemple/variadic.pl'])
				print('python/exemple/variadic.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/exemple/variadic.pl')

def testSundaram50(dd,gg):
	try:
		with open('python/function/Sundaram.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/Sundaram.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/Sundaram.pl'])
				print('python/function/Sundaram.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/Sundaram.pl')

def testautosubsets51(dd,gg):
	try:
		with open('python/function/autosubsets.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/autosubsets.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/autosubsets.pl'])
				print('python/function/autosubsets.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/autosubsets.pl')

def testcarre52(dd,gg):
	try:
		with open('python/function/carre.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/carre.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/carre.pl'])
				print('python/function/carre.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/carre.pl')

def testcarrecube53(dd,gg):
	try:
		with open('python/function/carrecube.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/carrecube.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/carrecube.pl'])
				print('python/function/carrecube.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/carrecube.pl')

def testdecomposition54(dd,gg):
	try:
		with open('python/function/decomposition.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/decomposition.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/decomposition.pl'])
				print('python/function/decomposition.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/decomposition.pl')

def testestpremier55(dd,gg):
	try:
		with open('python/function/estpremier.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/estpremier.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/estpremier.pl'])
				print('python/function/estpremier.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/estpremier.pl')

def testestpremier256(dd,gg):
	try:
		with open('python/function/estpremier2.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/estpremier2.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/estpremier2.pl'])
				print('python/function/estpremier2.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/estpremier2.pl')

def testfunctiongradertemplate57(dd,gg):
	try:
		with open('python/function/functiongradertemplate.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/functiongradertemplate.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/functiongradertemplate.pl'])
				print('python/function/functiongradertemplate.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/functiongradertemplate.pl')

def testfuncvoyelle58(dd,gg):
	try:
		with open('python/function/funcvoyelle.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/funcvoyelle.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/funcvoyelle.pl'])
				print('python/function/funcvoyelle.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/funcvoyelle.pl')

def testhistogramme159(dd,gg):
	try:
		with open('python/function/histogramme1.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/histogramme1.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/histogramme1.pl'])
				print('python/function/histogramme1.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/histogramme1.pl')

def testjumeaux60(dd,gg):
	try:
		with open('python/function/jumeaux.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/jumeaux.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/jumeaux.pl'])
				print('python/function/jumeaux.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/jumeaux.pl')

def testim61(dd,gg):
	try:
		with open('python/function/pim.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/pim.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/pim.pl'])
				print('python/function/pim.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/pim.pl')

def testimret62(dd,gg):
	try:
		with open('python/function/pimret.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/pimret.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/pimret.pl'])
				print('python/function/pimret.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/pimret.pl')

def testom63(dd,gg):
	try:
		with open('python/function/pom.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/pom.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/pom.pl'])
				print('python/function/pom.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/pom.pl')

def testracinecarre64(dd,gg):
	try:
		with open('python/function/racinecarre.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/racinecarre.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/racinecarre.pl'])
				print('python/function/racinecarre.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/racinecarre.pl')

def testrandomcolor165(dd,gg):
	try:
		with open('python/function/randomcolor1.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/randomcolor1.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/randomcolor1.pl'])
				print('python/function/randomcolor1.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/randomcolor1.pl')

def testromains66(dd,gg):
	try:
		with open('python/function/romains.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/romains.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/romains.pl'])
				print('python/function/romains.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/romains.pl')

def testromcode67(dd,gg):
	try:
		with open('python/function/romcode.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/romcode.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/romcode.pl'])
				print('python/function/romcode.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/romcode.pl')

def testsimplefunc168(dd,gg):
	try:
		with open('python/function/simplefunc1.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/simplefunc1.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/simplefunc1.pl'])
				print('python/function/simplefunc1.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/simplefunc1.pl')

def testsimplefunc269(dd,gg):
	try:
		with open('python/function/simplefunc2.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/simplefunc2.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/simplefunc2.pl'])
				print('python/function/simplefunc2.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/simplefunc2.pl')

def testsimplefunc370(dd,gg):
	try:
		with open('python/function/simplefunc3.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/simplefunc3.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/simplefunc3.pl'])
				print('python/function/simplefunc3.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/simplefunc3.pl')

def testsimplefunc471(dd,gg):
	try:
		with open('python/function/simplefunc4.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/simplefunc4.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/simplefunc4.pl'])
				print('python/function/simplefunc4.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/simplefunc4.pl')

def testsubsets72(dd,gg):
	try:
		with open('python/function/subsets.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/subsets.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/subsets.pl'])
				print('python/function/subsets.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/subsets.pl')

def testwritebase73(dd,gg):
	try:
		with open('python/function/writebase.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/function/writebase.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/function/writebase.pl'])
				print('python/function/writebase.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/function/writebase.pl')

def testageCapitaine74(dd,gg):
	try:
		with open('python/input/ageCapitaine.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/input/ageCapitaine.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/input/ageCapitaine.pl'])
				print('python/input/ageCapitaine.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/input/ageCapitaine.pl')

def testegalega75(dd,gg):
	try:
		with open('python/input/egalegal.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/input/egalegal.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/input/egalegal.pl'])
				print('python/input/egalegal.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/input/egalegal.pl')

def testusmoins76(dd,gg):
	try:
		with open('python/input/plusmoins.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/input/plusmoins.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/input/plusmoins.pl'])
				print('python/input/plusmoins.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/input/plusmoins.pl')

def testrint177(dd,gg):
	try:
		with open('python/input/print1.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/input/print1.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/input/print1.pl'])
				print('python/input/print1.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/input/print1.pl')

def testrint278(dd,gg):
	try:
		with open('python/input/print2.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/input/print2.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/input/print2.pl'])
				print('python/input/print2.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/input/print2.pl')

def testquelage79(dd,gg):
	try:
		with open('python/input/quelage.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/input/quelage.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/input/quelage.pl'])
				print('python/input/quelage.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/input/quelage.pl')

def testcommonelementsist80(dd,gg):
	try:
		with open('python/list/commonelementsist.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/list/commonelementsist.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/list/commonelementsist.pl'])
				print('python/list/commonelementsist.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/list/commonelementsist.pl')

def testireuneliste81(dd,gg):
	try:
		with open('python/list/lireuneliste.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/list/lireuneliste.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/list/lireuneliste.pl'])
				print('python/list/lireuneliste.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/list/lireuneliste.pl')

def testireunelisteint82(dd,gg):
	try:
		with open('python/list/lireunelisteint.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/list/lireunelisteint.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/list/lireunelisteint.pl'])
				print('python/list/lireunelisteint.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/list/lireunelisteint.pl')

def testsoussuite83(dd,gg):
	try:
		with open('python/list/soussuite.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/list/soussuite.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/list/soussuite.pl'])
				print('python/list/soussuite.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/list/soussuite.pl')

def testjumeaux84(dd,gg):
	try:
		with open('python/search/jumeaux.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/search/jumeaux.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/search/jumeaux.pl'])
				print('python/search/jumeaux.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/search/jumeaux.pl')

def teststackbasic85(dd,gg):
	try:
		with open('python/stack/stackbasic.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/stack/stackbasic.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/stack/stackbasic.pl'])
				print('python/stack/stackbasic.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/stack/stackbasic.pl')

def testundopile86(dd,gg):
	try:
		with open('python/stack/undopile.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/stack/undopile.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/stack/undopile.pl'])
				print('python/stack/undopile.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/stack/undopile.pl')

def testKolakoski87(dd,gg):
	try:
		with open('python/string/Kolakoski.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/string/Kolakoski.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/string/Kolakoski.pl'])
				print('python/string/Kolakoski.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/string/Kolakoski.pl')

def testcapitalize88(dd,gg):
	try:
		with open('python/string/capitalize.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/string/capitalize.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/string/capitalize.pl'])
				print('python/string/capitalize.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/string/capitalize.pl')

def testsort89(dd,gg):
	try:
		with open('python/string/sort.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/string/sort.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/string/sort.pl'])
				print('python/string/sort.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/string/sort.pl')

def testtemplate90(dd,gg):
	try:
		with open('python/template.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/template.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/template.pl'])
				print('python/template.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/template.pl')

def testtemplate91(dd,gg):
	try:
		with open('python/test/template.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/test/template.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/test/template.pl'])
				print('python/test/template.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/test/template.pl')

def testtuple192(dd,gg):
	try:
		with open('python/tuples/tuple1.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/tuples/tuple1.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/tuples/tuple1.pl'])
				print('python/tuples/tuple1.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/tuples/tuple1.pl')

def testtuple_template93(dd,gg):
	try:
		with open('python/tuples/tuple_template.pl',"r") as f:
			if not "0PLG" in f.read():
				print('python/tuples/tuple_template.pl',file=dd)
			else:
				subprocess.check_output([
				'python3','/Users/dr/DJANGO/plbank/pysrc/src/plcheck.py','python/tuples/tuple_template.pl'])
				print('python/tuples/tuple_template.pl',file=gg)

	except:
		assert 0
	print('pas de '+'python/tuples/tuple_template.pl')
