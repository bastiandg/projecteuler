#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Quadratic primes

import math

primes = []

def primeSieve(limit):
	numbers = []
	global primes
	primes = []
	for i in range(0, limit-1):
		numbers.append(True)

	for i in range(0, limit-1):
		if numbers[i] == True:
			p = i+2
			primes.append(p)
			for j in range(p*2,int(limit/p+1)*p,p):
				numbers[j-2] = False

def factorise(n):
	primeFactors = dict()
	while primes[-1] < n:
		expandPrimeSieve(primes[-1]*2)
		#print primes[-1]
	for p in primes:
		while n % p == 0:
			if not primeFactors.has_key(p):
				primeFactors[p] = 1
			else:
				primeFactors[p] += 1
			n /= p
		if n <= 1:
			break
	return primeFactors

def divisorCount(factors):
	count = 1
	for p in factors.keys():
		count *= (factors[p]+1)
	return count

def factors(primeFactors):
	count = divisorCount(primeFactors)
	primeBases = primeFactors.keys()
	factorList = []
	for i in range(count):
		factor = 1
		tmp = i
		for b in primeBases:
			power = (primeFactors[b] + 1)
			factor *= b ** (tmp % power)
			tmp /= power
		factorList.append(factor)
	return factorList

def factorSum(n):
	return sum(factors(factorise(n))) - n

limit = 1000
primeSieve(100000)


factorSumList = []
maxPrimeCount = 0
maxProduct = 0
max = 0

for i in range(-limit-1,limit+1,2):
	if i % 100 == 1:
		print i
	for j in primes:
		if j >= limit:
			break
		k = 0
		while True:
			if (k*k+i*k+j) not in primes:
				break
			k += 1
		if k > maxPrimeCount:
			maxPrimeCount = k
			maxProduct = i * j
			print "n² + %rn + %r => %r" % (i, j, k)
		k = 0
		while True:
			if (k*k+i*k-j) not in primes:
				break
			k += 1
		if k > maxPrimeCount:
			maxPrimeCount = k
			maxProduct = i * -j
			print "n² + %rn + %r => %r" % (i, j, k)

print maxProduct
