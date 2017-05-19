#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  doctestCcode.py
#  
#  Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
	"""
	Prend en parametre trois fichiers
	pltest les tests
	stub.py le fichier qui contient le stub python qui appel la fonction C
	student.c le fichier qui contient la fonction C
	
	cat >student.c <<EOF
	int f(){ return 3; }
	EOF
	gcc  -Wall -fPIC student.c -shared -Wl,-soname,librien.so.1 -o librien.so.1.0
	cat >stub.py <<EOF
	from ctypes import *
	cdll.LoadLibrary("./librien.so.1.0")
	librien=CDLL("./librien.so.1.0")
	def f():
		return librien.f()
	EOF
	
	"""
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
