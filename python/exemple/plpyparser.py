#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  plpyparser.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  
#  This program define the plparse(filename) function that return a dict of the pl file in argument
# 


from pyparsing import \
        Literal, Word, ZeroOrMore, Group, Dict, Optional, OneOrMore, \
        printables, ParseException, restOfLine, LineEnd, LineStart, FollowedBy,dictOf
import pprint


thegramma = None
def creategramma():
	# singleton patern utilité ??
	global thegramma
	if not thegramma:

		# punctuation

		equals = Literal("=").suppress()
		dequals   = Literal("==").suppress()
		sharp = Literal("#").suppress()
		comment = sharp + Optional( restOfLine )
		EOL = LineEnd().suppress()
		SOL = LineStart()

		doublequalsline=SOL+dequals+EOL

		# set for the word definition
		nonequals = "".join( [ c for c in printables if c != "=" ] ) + " \t"
		nonsharp = "".join( [ c for c in printables if c != "#" ] ) + " \t"

		lines = ZeroOrMore(SOL+ Group( nonequals+restOfLine)) # 

		# simple values   toto="truc"
		valueDef = equals + Group(nonequals+restOfLine)
		keyDef = Word(nonequals)+ FollowedBy("=")


		longDef = Word(nonequals) + dequals + lines + doublequalsline

		# using Dict will allow retrieval of named data fields as attributes of the parsed results
		thegramma = OneOrMore( dictOf(keyDef,valueDef)+EOL) # + ZeroOrMore( Group(longDef) )
		thegramma.ignore( comment )
		thegramma.setDebug( True )
	return thegramma


pp = pprint.PrettyPrinter(2)

def test( strng ):
	print( strng)
	try:
		with open(strng,"r") as iniFile :
			iniData = "".join( iniFile.readlines() )
			print(iniData)
			bnf = creategramma()
			tokens = bnf.parseString( iniData )
			pp.pprint( tokens.asList() )

	except ParseException as err:
		print( err.line)
		print( " "*(err.column-1) + "^")
		print( err)

	iniFile.close()
	print()
	return tokens
    

ini = test("queegal.pl")
