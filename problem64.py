#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Odd period square roots
import math
import numpy
from gmpy import is_square
from fractions import gcd

limit = 10000
oddCounter = 0
for n in range(1,limit + 1):
	#if True:
	#n = 9997
	if not is_square(n):
		a = []
		af = []
		ae = []
		ad = []

		a.append(int(math.sqrt(n)))
		ae.append(1)
		ad.append(-a[0])

		#for i in range(10):
		i = 0
		while True:
			if float(ae[i]*(math.sqrt(n) - ad[i])/(n - ad[i]**2)) in af:
				break
			else:
				af.append(float(ae[i]*(math.sqrt(n) - ad[i])/(n - ad[i]**2)))
			#print "%i / (√%i %i)" % (ae[i], n, ad[i])
			a.append(int(ae[i]*(math.sqrt(n) - ad[i])/(n - ad[i]**2)))
			d = gcd(ae[i], n - ad[i]**2)
			#print d
			#print "%i·(√%i + %i) / %i = %i" % (ae[i], n, -ad[i], n - ad[i]**2, a[1])
			x = ((-ad[i] * ae[i]) - (a[i+1] * (n - ad[i]**2)))/d
			#print x
			ae.append((n - ad[i]**2)/d)
			ad.append(x)
			i += 1
			#print "%i + (√%i + %i) / %i" % (a[i+1], n, ad[i+1], ae[i+1])
			#print "-----------------------"
		#print "%i %r" % (n, a[1:])
		#print af
		if len(a) % 2 == 0:
			oddCounter += 1

print oddCounter
