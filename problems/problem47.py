#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Distinct primes factors

limit = 1000000
import sys
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

def factorise(n):
	factors = dict()
	for p in primes:
		while n % p == 0:
			if not factors.has_key(p):
				factors[p] = 1
			else:
				factors[p] += 1
			n /= p
		if n <= 1:
			break
	return factors

primes = primeSieve(limit)

#for i in range(1,limit):
i = 99000
while i < limit:
	if (i % 1000) == 0:
		print i
	#print len(factorise(i).keys())
	#print factorise(i).keys()
	if len(factorise(i).keys()) >= 4:
		if len(factorise(i+1).keys()) >= 4:
			if len(factorise(i+2).keys()) >= 4:
				if len(factorise(i+3).keys()) >= 4:
					print "%r %r" % (i, factorise(i).keys())
					print "%r %r" % (i + 1, factorise(i + 1).keys())
					print "%r %r" % (i + 2, factorise(i + 2).keys())
					print "%r %r" % (i + 3, factorise(i + 3).keys())
					sys.exit(0)
				else:
					i += 4
			else:
				i += 3
		else:
			i += 2
	else:
		i += 1
