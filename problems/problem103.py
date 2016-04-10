#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Special subset sums: optimum

import itertools
import sys

setSums = dict()
for n in range(7, 8):
	setSums[n] = set()
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
					setSums[n].add(frozenset((frozenset(s1) , frozenset(s2))))

def subSetSumOrder(specialSet):
	for i in range(2, (len(specialSet) + 1) // 2 + 1):
		if sum(specialSet[:i]) <= sum(specialSet[-i + 1:]):
			return False
	return True

def subSetSumEquality(specialSet):
	for setSum in setSums[len(specialSet)]:
		sums = [0, 0]
		i = 0
		for indices in setSum:
			for j in indices:
				sums[i] += specialSet[j]
			i += 1
		if sums[0] == sums[1]:
			return False
	return True

specialSetSum = 0
it = 0

# I have guessed the ranges
for startElement in range(20, 22):
	for s in itertools.combinations(range(27, 52), 6):
		it += 1
		specialSet = tuple([startElement]) + s
		if subSetSumOrder(specialSet) and subSetSumEquality(specialSet):
			print(specialSet)
			print(it)
			sys.exit(0)
