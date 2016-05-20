template=@template.pl
title=Palindrom tester
title.fr=Testeur de palindrome
author=chilowi
text==
Write a function //is_palindrome// that tests if its single argument is a palindrom string, a palindrom string begin a string that can be identically read if read forwards or backwards (like "radar" or "detartrated").

The function can be employed to test any sequence (e.g the tuple (1,2,3,2,1) is considered as a palindrom).
==
text.fr==
Écrivez une fonction //is_palindrome// testant si son unique argument est une chaîne de caractères qui est un palindrome, i.e. qu'elle puisse se lire identiquement à l'endroit comme à l'envers (comme "radar" ou "detartrated").

La fonction doit pouvoir être utilisable pour tester si n'importe quelle séquence est un palyndrome (par exemple le tuple (1,2,3,2,1) est un palindrome).
==
code==
@arguments("radar")
@arguments("abracadabra")
@arguments("eluparunecrapule")
@arguments([1,2,3,2,1],
	expected_returned={
		(lambda x: isinstance(x, Exception)): 
			(0.0, i18n(_="Your function should work also with lists.\nHere is the encountered exception: {result.returned}", fr="Votre fonction doit fonctionner aussi avec les listes.\nVoici l'exception relevée: {result.returned}")),
		REFERENCE_RESULT: True
	})
@arguments([1,2,3])
@arguments("")
@arguments("detartrated")
def is_palindrome(x):
	return x[-1:-len(x)-1:-1] == x
==
badanswer1==
# Works only with strings
def get_reverse_string(x):
	reverse = ""
	i = len(x) - 1
	while i >= 0:
		reverse += x[i]
		i -= 1
	return reverse
	
def is_palindrome(x):
	return get_reverse_string(x) == x
==
