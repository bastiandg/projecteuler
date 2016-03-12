#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Prime digit replacements

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

def digits(n):
	digitList = []
	tmp = n
	while tmp >= 1:
		digitList.append(tmp%10)
		tmp /= 10
	return digitList

def numberFromDigitList(digitList):
	n = 0
	for i in range(len(digitList)):
		n += digitList[i] * 10**i
	return n

def sameDigits(digitList):
	sameDigitList = []
	for i in range(4):
		indices = []
		for j in range(len(digitList)):
			if i == digitList[j]:
				indices.append(j)
		if len(indices) > 1:
			sameDigitList.append(indices)
	return sameDigitList

primes = primeSieve(limit)
#exchangeDigits = [[2, 1], [3, 1], [3, 2], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4]]
primesTested = []
for p in primes:
	if p > (10**5):
		digitList = digits(p)
		exchangeDigits = sameDigits(digitList)
		for ed in exchangeDigits:
			exchangedPrimeList = []
			#print ed
			for i in range(10):
				for digit in ed:
					digitList[digit] = i
				n = numberFromDigitList(digitList)
				if n in primesTested:
					break
				if n in primes:
					exchangedPrimeList.append(n)
					primesTested.append(n)
				elif i == 0:
					primesTested.append(n)
			if len(exchangedPrimeList) >= 8:
				print "%i %r" % (len(exchangedPrimeList), exchangedPrimeList)

