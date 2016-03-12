#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Convergents of e

def digitSum(n, base):
	dSum = 0
	while n >= 1:
		dSum += n % base
		n /= base
	return dSum

a = [8, 11]
k = 4
for i in range(100):
	if i % 3 != 1:
		a.append(a[i] + a[i+1])
	else:
		a.append(a[i] + k * a[i + 1])
		k += 2
	print "%i %i %i" % (i+5, a[i+2], digitSum(a[i+2], 10))
