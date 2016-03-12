#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Even Fibonacci numbers

limit = 4000000
f1 = 1
f2 = 2
s = 0
while f1 < limit:
	#print f1
	if f1 % 2 == 0:
		s += f1
	tmp = f2
	f2 = f1 + f2
	f1 = tmp

print s
