#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Summation of primes
limit = 2000000
primes = []
numbers = []
primeSum = 0
for i in range(0, limit-1):
	numbers.append(True)

for i in range(0, limit-1):
	if numbers[i] == True:
		p = i+2
		#print " %r is prime, limit: %r" % ((i+2), int(limit/p)*p)
		primes.append(p)
		primeSum += p
		for j in range(p*2,int(limit/p+1)*p,p):
			numbers[j-2] = False

#for i in range(0, len(primes)):
	#print "%r: %r" % (i+1, primes[i])
print primeSum
