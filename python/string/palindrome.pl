template=@template.pl
title=Testeur de palindrome
author=chilowi
text==
Écrivez une fonction //is_palindrome// testant si son unique argument est une chaîne de caractères qui est un palindrome, i.e. qu'elle puisse se lire identiquement à l'endroit comme à l'envers (comme "radar" ou "detartrated").

La fonction doit pouvoir être utilisable pour tester si n'importe quelle séquence est un palyndrome (par exemple le tuple (1,2,3,2,1) est un palindrome).
==
answer==
@compare()
@arguments("radar")
@arguments("abracadabra")
@arguments("eluparunecrapule")
@arguments([1,2,3,2,1])
@arguments([1,2,3])
@arguments("")
@arguments("detartrated")
def is_palindrome(x):
	return x[-1:-len(x)-1:-1] == x
==
