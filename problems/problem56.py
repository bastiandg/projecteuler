#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Powerful digit sum

import math

def digitSum(n, base):
	dSum = 0
	while n >= 1:
		dSum += n % base
		n /= base
	return dSum

limit = 100

max = 0
for i in range(100):
	for j in range(100):
		ds = digitSum(i**j, 10)
		if ds > max:
			max = ds
			print "%i^%i = %i (%i)" % (i, j, i**j, ds)
print max

