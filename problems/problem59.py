#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Spiral primes

limit = 700000000
import sys
import math
import numpy
from bisect import bisect_left

def primeSieve(n):
	""" Input n>=6, Returns a array of primes, 2 <= p < n """
	sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
	for i in xrange(1,int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[       k*k/3     ::2*k] = False
			sieve[k*(k-2*(i&1)+4)/3::2*k] = False
	return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def f1(x):
	return x*x + x + 1

def f2(x):
	return x*x + 1

def f3(x):
	return x*x

def binarySearch(l, v):
	i = bisect_left(l, v)
	if i != len(l) and l[i] == v:
		return True
	else:
		return False

u = 1
inc = 1
length = 1
lengthLimit = int(math.sqrt(limit)/2)
#lengthLimit = limit
#lengthLimit = 10
primeCount = 0
corners = 1
primes = primeSieve(limit)

print lengthLimit

for i in range(1, lengthLimit):
	if binarySearch(primes, f1(i*2 - 1)):
		primeCount += 1
		#print f1(i*2 - 1)
	if binarySearch(primes, f2(i*2)):
		primeCount += 1
		#print f2(i*2)
	if binarySearch(primes, f1(i*2)):
		primeCount += 1
		#print f1(i*2)

	#print f3(i*2 + 1)
	length += 2
	corners += 4
	if ((length - 1) % 100) == 0:
		print "%i %r" % (i*2+1, (float(primeCount)/float(corners)))
	if (float(primeCount)/float(corners)) < 0.1:
		print length
		sys.exit(0)
	#u += inc
	#if (i % 2) == 0:
		#inc += 1
	#print u
	#if (i % 2) == 0:
		#print f2(i)
		#corners += 1
	#if (i % 2) == 1:
		#print f3(i)
		#corners += 1
	#print f1(i)
	#corners += 1
#print length
