#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Singular integer right triangles

import numpy
from fractions import gcd
import math
limit = 1500000

length = numpy.zeros(limit + 1, dtype=int)
for m in xrange(1, int(math.sqrt(limit)) + 1):
	for n in range(1, m): #int(limit/3)):
		a = m*m - n*n
		b = 2*m*n
		if gcd(a, b) == 1 and (a - b) % 2 == 1:
			l = 2 * m * (m + n)
			for i in xrange(l, limit + 1, l):
				length[i] += 1
		#print "%i, %i² + %i² = %i²" % (m*m - n*n + 2*m*n + m*m + n*n, m*m - n*n, 2*m*n, m*m + n*n)

counter = 0

for i in xrange(len(length)):
	if length[i] == 1:
		counter += 1
print counter
