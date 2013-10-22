#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Ordered fractions
from fractions import gcd

fraction = 3.0 / 7.0
limit = 1000000
closest = 0.0
closestFraction = (0, 1)
for i in xrange(2, limit + 1):
	for j in xrange(int(float(i) * fraction), 0, -1):
		if gcd(i, j) == 1:
			if float(j) / float(i) > closest and not (i == 7 and j == 3):
				closest = float(j) / float(i)
				closestFraction = (i , j)
			break
print fraction
print closest
print closestFraction
