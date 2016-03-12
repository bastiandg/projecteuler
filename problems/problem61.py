#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Cyclical figurate numbers
import sys
from sets import Set
import itertools

triangleSet = Set([])
squareSet = Set([])
pentagonalSet = Set([])
hexagonalSet = Set([])
heptagonalSet = Set([])
octagonalSet = Set([])
limit = 10000

def f3(x):
	return (x * (x + 1)) / 2

def f4(x):
	return x * x

def f5(x):
	return (x * (3 * x - 1)) / 2

def f6(x):
	return x * (2 * x - 1)

def f7(x):
	return (x * (5 * x - 3)) / 2

def f8(x):
	return x * (3 * x - 2)

def digits(n):
	digitList = []
	tmp = n
	while tmp >= 1:
		digitList.append(tmp%10)
		tmp /= 10
	digitList.reverse()
	return digitList

f = (f3, f4, f5, f6, f7, f8)
numSet = (triangleSet, squareSet, pentagonalSet, hexagonalSet, heptagonalSet, octagonalSet)

for i in range(len(f)):
	j = 1
	while f[i](j) < 10000:
		if f[i](j) > 1000:
			numSet[i].add(f[i](j))
		j += 1

for ns in itertools.permutations(numSet):
	for i in ns[0]:
		for i2 in ns[1]:
			if digits(i)[-2:] == digits(i2)[:2]:
				for i3 in ns[2]:
					if digits(i2)[-2:] == digits(i3)[:2]:
						for i4 in ns[3]:
							if digits(i3)[-2:] == digits(i4)[:2]:
								for i5 in ns[4]:
									if digits(i4)[-2:] == digits(i5)[:2]:
										for i6 in ns[5]:
											if digits(i5)[-2:] == digits(i6)[:2] and digits(i6)[-2:] == digits(i)[:2]:
												print "TADA %i %i %i %i %i %i !!!" % (i, i2, i3, i4, i5, i6)
												print "%i" % (i + i2 + i3 + i4 + i5 + i6)


