#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Digit factorials

import math

base = 10

def factorialSum(n):
	fs = 0
	while n >= 1:
		fs += math.factorial(n%base)
		n /= base
	return fs

limit = 1000000
totalSum = 0

for i in range(3, limit):
	if i == factorialSum(i):
		print i
		totalSum += i

print totalSum
