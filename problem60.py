#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Spiral primes

limit = 10000
primeLimit = 100000000
import sys
import math
import numpy
import itertools
from bisect import bisect_left

def primeSieve(n):
	""" Input n>=6, Returns a array of primes, 2 <= p < n """
	sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
	for i in xrange(1,int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[       k*k/3     ::2*k] = False
			sieve[k*(k-2*(i&1)+4)/3::2*k] = False
	return numpy.r_[3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def binarySearch(l, v):
	i = bisect_left(l, v)
	if i != len(l) and l[i] == v:
		return True
	else:
		return False

def concat(a, b):
	return int(a * 10 ** math.ceil(math.log10(b)) + b)

combinationPrimes = primeSieve(limit)
primes = primeSieve(primeLimit)
print "primes collected"
#startPrimes = [3, 7, 109, 673]
print primes[-1]
print concat(combinationPrimes[-1], 673)
combinations2 = []
#del(primes[0])

#firstNum = 2
for primeCombination in itertools.combinations(combinationPrimes, 2):
	#awesome = True
	#for combination in itertools.combinations(primeCombination, 2):
		#if not binarySearch(primes, concat(combination[0], combination[1])) or not binarySearch(primes, concat(combination[1], combination[0])):
			#awesome = False
			#break
	#if awesome:
		#combinations2.append(primeCombination)
	if binarySearch(primes, concat(primeCombination[0], primeCombination[1])) and binarySearch(primes, concat(primeCombination[1], primeCombination[0])):
		combinations2.append(primeCombination)

print "combinations2 collected"
print len(combinations2)
print type(combinations2[0])
c2 = set(combinations2)
combinations3 = []

#for i in range(len(combinations2)):
	#for j in range(i + 1, len(combinations2)):
		#if combinations2[i][1] == combinations2[j][0] and (combinations2[i][0], combinations2[j][1]) in c2:
			#combinations3.append((combinations2[i][0], combinations2[i][1], combinations2[j][1]))
		#elif combinations2[i][1] < combinations2[j][0]:
			#break

print "l2 = %i" % len(combinations2)
print type(combinations2[0])
print combinations2[0:10]

for combination in combinations2:
	for p in combinationPrimes:
		if p > combination[-1] and p not in combination:
			awesome = True
			for c in combination:
				#print c
				if c < p and (c, p) not in c2 or c > p and (p, c) not in c2:
					awesome = False
			if awesome:
				#print "%r %i" % (combination, p)
				combinations3.append(combination + (p,))

print "l3 = %i" % len(combinations3)
print type(combinations3[0])
print combinations3[0:10]

combinations4 = []
for combination in combinations3:
	for p in combinationPrimes:
		if p > combination[-1] and p not in combination:
			awesome = True
			for c in combination:
				#print c
				if c < p and (c, p) not in c2 or c > p and (p, c) not in c2:
					awesome = False
			if awesome:
				combinations4.append(combination + (p,))

print "l4 = %i" % len(combinations4)
print type(combinations4[0])
print combinations4[0:10]
combinations5 = []
for combination in combinations4:
	for p in combinationPrimes:
		if p > combination[-1] and p not in combination:
			awesome = True
			for c in combination:
				if c < p and (c, p) not in c2 or c > p and (p, c) not in c2:
					awesome = False
			if awesome:
				combinations5.append(combination + (p,))

print len(combinations5)
print combinations5
print sum(combinations5[0])
