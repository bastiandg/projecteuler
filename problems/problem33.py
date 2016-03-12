#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Digit canceling fractions
import math
from fractions import gcd

def commonDigits(a, b):
	digitsA = []
	digitsB = []
	while a >= 1:
		digitsA.append(a%10)
		a /= 10
	while b >= 1:
		digitsB.append(b%10)
		b /= 10
	return list(set(digitsA).intersection(digitsB))

def wrongSimplification(a, b, c):
	if c == 0:
		return 1
	if a % 10 == c:
		a /= 10
	else:
		a -= c*10
	if b % 10 == c:
		b /= 10
	else:
		b -= c*10
	if b == 0:
		return 1
	return float(a)/float(b)

numerator = 1
denominator = 1
for i in range(10,100):
	for j in range(i+1,100):
		digits = commonDigits(i, j)
		for digit in digits:
			if wrongSimplification(i, j, digit) == float(i)/float(j):
				print "%r / %r" % (i, j)
				numerator *= i
				denominator *= j

print denominator/gcd(numerator,denominator)
