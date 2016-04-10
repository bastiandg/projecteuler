#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Special subset sums: meta-testing

import itertools

# https://stackoverflow.com/a/4941932
def ncr(n, r):
	r = min(r, n - r)
	if r == 0:
		return 1
	numer = 1
	for i in range(n, n - r, -1):
		numer *= i
	denom = 1
	for i in range(1, r + 1):
		denom *= i
	return numer // denom

n = 7
pSum = 0
for i in range(2, n // 2 + 1):
	for s1 in itertools.combinations(range(n), i):
		x = sorted(set(range(n)) - set(s1))
		for s2 in itertools.combinations(x, i):
			smaller = False
			bigger = False
			for j in range(i):
				if s1[j] > s2[j]:
					bigger = True
				else:
					smaller = True
			if smaller and bigger:
				pSum += 1

print(pSum // 2)
