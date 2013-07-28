#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Consecutive prime sum

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

primes = primeSieve(limit)

max = 0

for i in range(len(primes)):
	consecutiveSum = 0
	for j in range(i, len(primes)):
		consecutiveSum += primes[j]
		if (consecutiveSum % 2 != 0) and consecutiveSum in primes and (j - i + 1) > max:
			print "%i + ... + %i = %i (%i)" % (primes[i], primes[j], consecutiveSum, j - i + 1)
			max = j - i + 1
		if consecutiveSum > limit:
			break
