#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Non-abundant sums

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

limit = 28123
primeSieve(limit+100)

notSummableSum = 0
notSummableList = []

for i in range(limit):
	notSummableList.append(True)

abundantList = []

for i in range(2,limit+1):
	fs = factorSum(i)
	if fs > i:
		abundantList.append(i)

for i in abundantList:
	for j in abundantList:
		if (i+j) < limit:
			notSummableList[i+j] = False
		else:
			break

for i in range(1,limit):
	if notSummableList[i] == True:
		notSummableSum += i

print notSummableSum

#for i in range(2,limit+1):
	#if factorSumList[i-2] <= limit-2:
		#if factorSumList[factorSumList[i-2]-2] == i and factorSumList[i-2] != i:
			#amicSum += i
			#print "%r <=> %r" % (factorSumList[i-2], i)
