#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Counting fractions in a range
from fractions import gcd
import math

limit = 12000
fractionCounter = 0
for i in xrange(2, limit + 1):
	for j in xrange(int(math.ceil(float(i) / 3.0)), int(i / 2) + 1):
		if gcd(i, j) == 1 and j != 1:
			fractionCounter += 1
print fractionCounter
