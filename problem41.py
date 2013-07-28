#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Pandigital prime

base = 10
limit = 7654321
#Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
#Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)

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

def expandPrimeSieve(limit):
	numbers = []
	for i in range(limit):
		numbers.append(True)
	numberStart = primes[-1] + 1
	for p in primes:
		searchStart = int(math.ceil(float(numberStart)/float(p))*p)
		searchStop = int((numberStart+limit-1)/p+1)*p
		for j in range(searchStart, searchStop, p):
			numbers[j-numberStart] = False

	for i in range(numberStart, primes[-1]+limit+1):
		if numbers[i-numberStart] == True:
			p = i
			searchStart = int(math.ceil(float(numberStart)/float(p))*p)
			searchStop = int((numberStart+limit-1)/p+1)*p
			primes.append(p)
			for j in range(searchStart, searchStop, p):
				numbers[j-numberStart] = False

def isPandigital(n):
	digits = []
	while n >= 1:
		digits.append(n % base)
		n /= base
	i = 0
	finished = False
	while not finished and i < 10:
		i += 1
		if i not in digits:
			finished = True

	#if len(set(digits)) == i-1: # and not finished:
	if len(digits) == len(set(digits)) and len(digits) == i-1:
		return True
	else:
		return False

primes = primeSieve(limit)
print "aaaa"
for p in primes:
	if isPandigital(p):
		print p
