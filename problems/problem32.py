#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Pandigital products

base = 10
pandigitalSum = 0
pandigitalList = []

def isPandigital(n1, n2, n3):
	digits = []
	while n1 >= 1:
		digits.append(n1%base)
		n1 /= base
	while n2 >= 1:
		digits.append(n2%base)
		n2 /= base
	while n3 >= 1:
		digits.append(n3%base)
		n3 /= base
	if len(digits) == (base - 1) and len(set(digits)) == (base - 1) and 0 not in digits:
		return True
	else:
		return False

for i in range(1,500):
	for j in range(i+1,5000):
		if isPandigital(i, j, i*j):
			print "%r * %r = %r" % (i, j, i*j)
			if (i * j) not in pandigitalList:
				pandigitalSum += i*j
				pandigitalList.append(i*j)

print pandigitalSum
