#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Diophantine reciprocals II

from fractions import gcd
import time

maxPrime = 1000
n = 4000000
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

def primeProduct(primeFactors):
	p = 1
	for i in range(len(primeFactors)):
		p *= primes[i] ** primeFactors[i]
	return p

def fractionCount(primeFactors):
	fc = 1
	for c in primeFactors:
		fc += (2 * fc - 1) * c
	return fc

def productIterator(max, index, primeFactors):
	if primeProduct(primeFactors) > max:
		pass
	elif primeProduct(primeFactors) == max:
		yield primeFactors
	else:
		yield primeFactors
		p2 = list(primeFactors)
		p2[index + 1] = 1
		for p in productIterator(max, index + 1, p2):
			yield p
		p2 = list(primeFactors)
		if index == 0 or (index != 0 and primeFactors[index] < primeFactors[index - 1]):
			p2[index] += 1
			for p in productIterator(max, index, p2):
				yield p

primeSieve(maxPrime)
resultList = []
for exp in range(1000):
	for p in productIterator(2 ** exp, 0, [1] + [0] * 19):
		if fractionCount(p) > n:
			resultList.append(primeProduct(p))
	if len(resultList) > 0:
		for result in sorted(resultList):
			print(result)
		break

