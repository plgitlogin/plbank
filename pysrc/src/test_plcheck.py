

import plcheck
import plrequest
import pytest
import json

#FIXME can't test exceptions with pytest 
#def test_plcheck_basic_error1():
	#plcheck.main(plcheck.getrepodir(),"debug1.pl")
	#with raises(FileNotFoundError) :
		#s= plrequest.SanboxSession(q,"http://pl-sandbox-test.u-pem.fr/?action=execute")



def test_plcheck_basic2():
	answer =plcheck.main(plcheck.getrepodir(),"debug2.pl",sandboxurl="http://pl-sandbox-test.u-pem.fr/?action=execute",studentfile="print(4)")

	result = json.loads(answer)
	print(answer)
	assert result["platform_error"]==[]
