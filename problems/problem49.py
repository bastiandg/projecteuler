#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Distinct primes factors

limit = 10000
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

def digits(n):
	digitList = []
	tmp = n
	while tmp >= 1:
		digitList.insert(0,tmp%10)
		tmp /= 10
	if n < 100:
		digitList.insert(0,0)
		if n < 10:
			digitList.insert(0,0)
	return digitList

primes = primeSieve(limit)
for p in primes:
	if p > 999:
		permutationList = [p]
		for p2 in primes:
			if p2 > p and sorted(digits(p)) == sorted(digits(p2)) and p != p2:
				permutationList.append(p2)
			#distances = []
			for i in range(1,len(permutationList) - 1):
				distance = permutationList[i] - permutationList[0]
				if (permutationList[i] + distance) in permutationList:
					print "%i %i %i" % (permutationList[0], permutationList[i], permutationList[i] + distance)
		#if len(permutationList) >= 4: #or p == 1487: # and permutationList[1] - permutationList[0] == permutationList[2] - permutationList[1]:
			#print permutationList


