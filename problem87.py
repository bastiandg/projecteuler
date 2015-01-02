#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Prime power triples

import math
import numpy

def primeSieve(n):
	""" Input n>=6, Returns a array of primes, 2 <= p < n """
	sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
	for i in xrange(1,int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[       k*k/3     ::2*k] = False
			sieve[k*(k-2*(i&1)+4)/3::2*k] = False
	return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

max = 50000000
counter = 0
se = set()

squarePrimes = primeSieve(max ** (1.0 / 2.0) + 1)
cubePrimes = primeSieve(max ** (1.0 / 3.0) + 1)
fourthPowerPrimes =  primeSieve(max ** (1.0 / 4.0) + 1)

for p2 in squarePrimes:
	for p3 in cubePrimes:
		for p4 in fourthPowerPrimes:
			if p2 ** 2 + p3 ** 3 + p4 ** 4 < max:
				counter += 1
				se.add(p2 ** 2 + p3 ** 3 + p4 ** 4)

print counter
print len(se)
