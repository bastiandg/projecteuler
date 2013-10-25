#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Digit factorial chains

import math

limit = 1000000
base = 10
recursionLength = 60
factorialSumList = dict()
counter = 0

def factorialSum(loop, n, depth):
	global counter
	if not factorialSumList.has_key(n):
		tmp = n
		fs = 0
		while tmp >= 1:
			fs += math.factorial(tmp % base)
			tmp /= base
		factorialSumList[n] = fs
	else:
		fs = factorialSumList[n]
	if fs in loop:
		if depth == recursionLength:
			counter += 1
		else:
			return
	elif depth < recursionLength + 1:
		loop.append(fs)
		factorialSum(loop, fs, depth + 1)


factorialSumList[0] = 1
for i in xrange(1, limit + 1):
	factorialSum([i], i, 1)

print counter
