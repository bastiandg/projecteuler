#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Truncatable primes

import math
import sys

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

def expandPrimeSieve(limit):
	numbers = []
	for i in range(limit):
		numbers.append(True)
	numberStart = primes[-1] + 1
	for p in primes:
		searchStart = int(math.ceil(float(numberStart)/float(p))*p)
		searchStop = int((numberStart+limit-1)/p+1)*p
		for j in range(searchStart, searchStop, p):
			numbers[j-numberStart] = False

	for i in range(numberStart, primes[-1]+limit+1):
		if numbers[i-numberStart] == True:
			p = i
			searchStart = int(math.ceil(float(numberStart)/float(p))*p)
			searchStop = int((numberStart+limit-1)/p+1)*p
			primes.append(p)
			for j in range(searchStart, searchStop, p):
				numbers[j-numberStart] = False

def factorise(n):
	factors = dict()
	while primes[-1] < n:
		expandPrimeSieve(primes[-1]*2)
		print primes[-1]
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

def printPrimeFactorisation(factors):
	product = 1
	string = ""
	for p in factors.keys():
		product = product * p ** factors[p]
		string += "%r^%r * " % (p, factors[p])
	print "%s = %r" % (string[0:-3], product)

def divisorCount(factors):
	count = 1
	for p in factors.keys():
		count *= (factors[p]+1)
	return count

def truncate(n):
	truncList = [n]
	digits = int(math.ceil(math.log10(n)))
	for i in range(1, digits):
		truncList.append(n/(10**i))
		#print int(n/10**i)*10**i
		truncList.append(n - (int(n/10**i)*10**i))
	return truncList

primeSieve(10**6)
truncPrimeSum = 0

for p in primes:
	#print p
	truncList = truncate(p)
	#print circleList
	truncPrime = True
	for n in truncList:
		if n not in primes:
			truncPrime = False
			break
	if truncPrime and p not in [2, 3, 5, 7]:
		print truncList
		truncPrimeSum += p
		#for n in circleList:
			#circlePrimeSum += n
			#if n in primes:
				#print primes[:10]
				#primes.remove(n)

print truncPrimeSum
