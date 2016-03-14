#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Amicable chains

import math
import time

maximum = 10 ** 6
primes = []
primeFactorList = [None] * (maximum + 1)
factorSumList = [0] * (maximum + 1)

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

def primeFactors(n, pl, start):
	primeFactorList[n] = pl
	stop = int(maximum / n)
	for i in range(start, len(primes)):
		if primes[i] > stop:
			return
		pl2 = dict(pl)
		if primes[i] in pl2.keys():
			pl2[primes[i]] += 1
		else:
			pl2[primes[i]] = 1
		primeFactors(n * primes[i], pl2, i)
	return

def factors(n):
	primeFactors = primeFactorList[n]
	count = divisorCount(primeFactors)
	primeBases = primeFactors.keys()
	factorList = []
	for i in range(count):
		factor = 1
		tmp = i
		for b in primeBases:
			power = (primeFactors[b] + 1)
			factor *= b ** (tmp % power)
			tmp = int(tmp / power)
		factorList.append(factor)
	return factorList

def divisorCount(factors):
	count = 1
	for p in factors.keys():
		count *= (factors[p]+1)
	return count

def factorSum(n):
	return sum(factors(n)) - n

primeSieve(maximum)
s = time.time()
primeFactors(1, dict(), 0)
for i in range(1, maximum):
	if i % 1000 == 0:
		print(i)
	factorSumList[i] = factorSum(i)

maxLen = 0
maxChain = []
d = time.time()
for i in range(1, maximum):
	chain = [i]
	fs = factorSumList[i]
	while fs not in chain and fs != 1:
		chain.append(fs)
		if fs > maximum:
			chain = []
			break
		fs = factorSumList[fs]
	if fs == i and len(chain) > maxLen:
		maxLen = len(chain)
		maxChain = chain
print(time.time() - d)

print(maxChain)
print(min(maxChain))
