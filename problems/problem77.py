#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Counting summations

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


def f(l, N):
	a = [1]+[0]*N
	for i in l:
		for j in range(N-i+1):
			a[i+j] += a[j]
	return a[-1]

limit = 5000
s = 0
i = 1
while s < limit:
	s = f(primeSieve(i + 1), i)
	print "%i: %i" % (i, s)
	i += 1
