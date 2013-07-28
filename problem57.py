#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Square root convergents

import math

limit = 1000
numerator = 3
denominator = 2
counter = 0

for i in range(limit):
	numerator = numerator + 2 * denominator
	denominator = numerator - denominator
	#print "%i (%i) / %i (%i)" % (numerator, int(math.log10(numerator)), denominator, int(math.log10(denominator)))
	if int(math.log10(numerator)) > int(math.log10(denominator)):
		counter += 1
print counter
