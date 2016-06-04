#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Diophantine reciprocals I

import math
import sys
from fractions import gcd

maximum = 10 ** 6
diophantineSolutions = [0]
primeFactorList = [None] * (maximum + 1)
divisorCountList = [0] * (maximum + 1)
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

def fractionCount(n):
	factorList = factors(n)
	fc = 0
	for i in range(len(factorList) - 1, -1, -1):
		for j in range(i, -1, -1):
			# if n == 4:
				# print("%i %i - %.2f" % (factorList[i], factorList[j], factorList[i] / factorList[j]))
			if gcd(factorList[i], factorList[j]) == 1:
				# print("%i %i - %.2f" % (factorList[i], factorList[j], factorList[i] / factorList[j]))
				fc += 1
	return fc


primeSieve(maximum)
primeFactors(1, dict(), 0)
maxDivisors = 0

for i in range(1, maximum):
	fc = fractionCount(i)
	if fc > 1000:
		print("%5i %4i" % (i, fc))
		print(primeFactorList[i])
		sys.exit()

# for n in range(1, 30):
	# solutions = 0
	# for i in range(n, 2 * n + 1):
		# for j in range(n * (n + 1) + 1, i - 1, -1):
			# if n * (i + j) == i * j:
				# solutions += 1
				# print("%4i %4i %.2f" % (i, j, j / i))
				# break
	# print("%2i: %i" % (n, solutions))
	# if solutions > 100:
		# print(n)
