#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Diophantine equation
import math
from gmpy import is_square
from fractions import gcd

limit = 1000
a = []
#for d in range(1, limit + 1):
	##print d
	#if not isSquare(d):# and d not in (61, 73, 97, 106):
		#x = d + 1
		#while not (is_square(x) and is_square((x - 1) / d)):
			#x += d
		#print "%i %i - %i" % (d, math.sqrt(x), (x - 1)/d) #int(math.sqrt(d * y**2 + 1)))

def squarePeriod(n):
	if not is_square(n):
		a = []
		af = []
		ae = []
		ad = []

		a.append(int(math.sqrt(n)))
		ae.append(1)
		ad.append(-a[0])

		i = 0
		while True:
			if float(ae[i]*(math.sqrt(n) - ad[i])/(n - ad[i]**2)) in af:
				break
			else:
				af.append(float(ae[i]*(math.sqrt(n) - ad[i])/(n - ad[i]**2)))
			a.append(int(ae[i]*(math.sqrt(n) - ad[i])/(n - ad[i]**2)))
			d = gcd(ae[i], n - ad[i]**2)
			ae.append((n - ad[i]**2)/d)
			ad.append(((-ad[i] * ae[i]) - (a[i+1] * (n - ad[i]**2)))/d)
			i += 1
		return a
	else:
		return []

for i in range(limit + 1):
	period = squarePeriod(i)
	if len(period) > 0:
		enumerator = []
		denominator = []
		#print period
		enumerator.append(period[0])
		denominator.append(1)
		enumerator.append(period[0] * period[1] + 1)
		denominator.append(period[1])
		if (enumerator[0]**2 - i * denominator[0]**2) == 1:
			#print "%i: %i² - %i·%i² = 1" % (i, enumerator[0], i, denominator[0])
			a.append(enumerator[0])
		elif (enumerator[1]**2 - i * denominator[1]**2) == 1:
			a.append(enumerator[1])
			#print "%i: %i² - %i·%i² = 1" % (i, enumerator[1], i, denominator[1])
		else:
			l = len(period) - 1
			j = 2
			while True:
				k = j & 1
				enumerator[k] = enumerator[k] + enumerator[k^1] * period[(j - 1) % l + 1]
				denominator[k] = denominator[k] + denominator[k^1] * period[(j - 1) % l + 1]
				#print "%i/%i ~ %f" % (enumerator[k], denominator[k], float(float(enumerator[k])/float(denominator[k])))
				j += 1
				if (enumerator[k]**2 - i * denominator[k]**2) == 1:
					a.append(enumerator[k])
					#print "%i: %i² - %i·%i² = 1" % (i, enumerator[k], i, denominator[k])
					break
print max(a)
