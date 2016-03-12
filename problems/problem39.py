#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Integer right triangles

import math
counter = dict()

finished = False
limit = 1000

def isSquare(n):
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

for a in range(1, limit/2):
	for b in range(1, limit/2):
		#p = (i**2 - j**2) + (2*i*j) + (i**2 + j**2)
		c2 = a**2 + b**2
		if isSquare(c2):
			p = a + b + int(math.sqrt(c2))
			if p < limit:
				if counter.has_key(p):
					counter[p] += 1
				else:
					counter[p] = 1
				#print "%r^2 + %r^2 = %r^2" % (i**2 - j**2, 2*i*j, i**2 + j**2)

max = 0
for key in counter.keys():
	if counter[key] > max:
		max = counter[key]
		print key
