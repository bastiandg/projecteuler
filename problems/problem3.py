#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Largest prime factor

import math
iterations = 0
n = 600851475143
primeFactors = []
nTmp = n
dividerStart = 2
divided = True

while divided == True and nTmp > 1:
	divided = False
	for i in range(dividerStart, int(math.sqrt(nTmp))) or divided:
		iterations+=1
		if nTmp % i == 0:
			dividerStart = i
			primeFactors.append(i)
			nTmp /= i
			divided = True

print "Prime factors of %i : %r " % (n, primeFactors)
print iterations

