#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Special Pythagorean triplet

pSum = 1000

for a in range(1,pSum-2):
	for c in range(pSum-2-a, 0, -1):
		b = pSum -a -c
		if (a**2 + b**2) == c**2:
			"Pythagorean triplet!"
			print "%r² +  %r² =  %r" % (a, b, c)
			print "%r*%r*%r = %r" % (a, b, c, a*b*c)
