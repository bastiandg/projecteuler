#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Smallest multiple

import math
limit = 20
primeListTotal = []
for i in range(0,limit):
	primeListTotal.append(0)

for i in range (2,limit+1):
	iterations = 0
	n = i
	primeList = []
	nTmp = n
	dividerStart = 2
	divided = True

	for j in range(0,limit):
		primeList.append(0)

	while divided == True and nTmp > 1:
		divided = False
		f = dividerStart
		while f <= int(math.sqrt(nTmp)) and not divided:
			iterations+=1
			if nTmp % f == 0:
				dividerStart = f
				primeList[f] += 1
				nTmp /= f
				divided = True
			else:
				f += 1
	if nTmp > 1:
		primeList[nTmp] += 1
	print "%r: %r" % (n, primeList)
	for j in range(0,limit):
		if primeList[j] > primeListTotal[j]:
			primeListTotal[j] = primeList[j]

total = 1
for i in range(len(primeListTotal)):
	if i > 0:
		print "%r *  %r ^ %r = %r" % (total, i, primeListTotal[i], total* i**primeListTotal[i])
	total *= i**primeListTotal[i]
print primeListTotal
print total
