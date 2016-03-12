#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Product-sum numbers

import sys
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

def printPrimeFactors(factors):
	product = 1
	string = ""
	for p in factors.keys():
		product = product * p ** factors[p]
		string += "%r^%r * " % (p, factors[p])
	print "%5i = %s" % (product, string[0:-3])

def primeFactors(n):
	factors = dict()
	while primes[-1] < n:
		print "prime error"
		sys.exit(0)
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

def divisorCount(factors):
	count = 1
	for p in factors.keys():
		count *= (factors[p]+1)
	return count

def factors(n):
	primeFactorList = primeFactors(n)
	count = divisorCount(primeFactorList)
	primeBases = primeFactorList.keys()
	factorList = []
	for i in range(count):
		factor = 1
		tmp = i
		for b in primeBases:
			power = (primeFactorList[b] + 1)
			factor *= b ** (tmp % power)
			tmp /= power
		factorList.append(factor)
	return factorList[1:]

def factorisation(n):
	factorisationTmp = []
	for factor in factors(n):
		for lst in factorisations[n / factor]:
			factorTuple = sorted(tuple(lst) + tuple([factor]))
			if factorTuple[0] == 1:
				del(factorTuple[0])
			factorisationTmp.append(tuple(factorTuple))
	factorisations.append(set(factorisationTmp))
factorisations = [[[]],[tuple([1])],[tuple([2])],[tuple([3])]]

max = 12000
productSumLength = [0] * (max + 1)
primes = primeSieve(int(max * 2))

for i in range(4, int(max * 1.2)):
	factorisation(i)

for i in range(4, int(max * 1.2)):
	for factorList in factorisations[i]:
		if len(factorList) != 1:
			length = (i - sum(factorList) + len(factorList))
			if length <= max and productSumLength[length] == 0:
				productSumLength[length] = i

print sum(set(productSumLength))
