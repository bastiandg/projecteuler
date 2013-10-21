#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Counting fractions
import numpy
import time
import math
from bisect import bisect_left

limit = 1000000
def primeSieve(n):
	""" Input n>=6, Returns a array of primes, 2 <= p < n """
	sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
	for i in xrange(1,int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[       k*k/3     ::2*k] = False
			sieve[k*(k-2*(i&1)+4)/3::2*k] = False
	return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def totient(factors):
	t = 1
	for factor in factors.keys():
		t *= (factor ** (factors[factor] - 1)) * (factor - 1)
	return t

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

def generate(n, factors, maxFactor):
	#print n
	t1 = time.time()
	totients[n] = totient(factors)
	times.append(time.time() - t1)
	if isPermutation(totients[n], n):
		permList.append(float(n)/float(totients[n]))
		intList.append(n)
	#if n == 4:
		#print factors
	#if len(totients) % 10000 == 0:
		#print len(totients)
		#print numpy.mean(times) * 1000
	#start = numpy.where(primes==maxFactor)[0]
	start = bisect_left(primes, maxFactor)
	#print start
	i = start
	#for i in range(start, len(primes)):
	while i < len(primes):
		if n * primes[i] <= limit:
			f = dict(factors)
			if primes[i] in f.keys():
				f[primes[i]] += 1
			else:
				f[primes[i]] = 1
			generate(n * primes[i], f, primes[i])
		else:
			break
		i += 1

def digits(n):
	digitList = []
	tmp = n
	while tmp >= 1:
		digitList.append(tmp%10)
		tmp /= 10
	return digitList

def isPermutation(a, b):
	return sorted(digits(a)) == sorted(digits(b))

#print isPermutation(87109, 79081)
times = []
permList = []
intList = []

primes = primeSieve(limit)
print "primes collected"
#totients = [None, 1]
#totients[1] = 1
totients = numpy.empty(limit + 1, dtype=int)
for p in primes:
	factors = dict()
	factors[p] = 1
	generate(p, factors, p)
#print totients
#for i in range(1, 101):
	#print "%i %i" % (i, totients[i])
#print totients[100]
#print intList[permList.index(max(permList))]
print sum(totients)
