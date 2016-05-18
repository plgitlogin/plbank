
import sys
import json 
import doctest

dico_good = { "success": True , "errormessages" : "" , "execution": "OK", "feedback": "ok", "other": "" }
dico_bad = { "success": False , "errormessages" : "création d'une exception", "execution": "", "feedback": "modifier votre valeur", "other": "" }

__doc__=""">>> from student import foobar
>>> foobar(3)
'Fizz'
>>> foobar(7)
'Buzz'
>>> foobar(33/0)
'Fizz Buzz'
>>> foobar(11)
>>> 
"""


failures,tests = doctest.testmod()
if failures == 0:
	print(json.dumps(dico_good))
else:
	print(dico_bad)
