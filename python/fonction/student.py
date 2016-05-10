
__doc__=""">>>foobar(1)
>>>"""

def foobar(n):
	""">>>foobar(1)
	>>>"""
	if n % 3 ==0 and  n %7 == 0:
		return "Fizz Buzz"
	if n % 3 == 0:
		return "Fizz"
	if n % 7 == 0:
		return "Buzz"
