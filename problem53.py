#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Combinatoric selections

import math

limit = 100

def nCr(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

millionCounter = 0
for i in range(limit + 1):
	for j in range(i + 1):
		if nCr(i, j) > 1000000:
			millionCounter += 1

print millionCounter
