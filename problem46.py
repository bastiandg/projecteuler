#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Goldbach's other conjecture

limit = 100000
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

def components(n):
	#print "%i ---- " % n
	for p in primes:
		if p > n:
			return None, None
		a = int(math.sqrt((n - p) / 2))
		#print (p + 2 * a * a)
		if (p + 2 * a * a) == n:
				return n, a
	return 1, 1


primes = primeSieve(limit)

for i in range(9, limit + 1, 2):
	if i not in primes:
		c1, c2 = components(i)
		if not c1:
			print i

