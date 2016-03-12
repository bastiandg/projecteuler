#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Cyclical figurate numbers
import sys
from sets import Set
import itertools

def digits(n):
	digitList = []
	tmp = n
	while tmp >= 1:
		digitList.append(tmp%10)
		tmp /= 10
	digitList.reverse()
	return digitList

def digitListToNum(digitList):
	n = 0
	for i in range(len(digitList)):
		n += digitList[i] * 10 ** (len(digitList) - i - 1)
	return n


limit = 10000

cubes = []

for i in range(limit):
	cubes.append(digits(i ** 3))

for i in range(limit):
	cubePermutations = 0
	for j in range (i, limit):
		if len(cubes[j]) > len(cubes[i]):
			break
		if sorted(cubes[i]) == sorted(cubes[j]):
			cubePermutations += 1
	if cubePermutations >= 5:
		print "%i - %i" % (digitListToNum(cubes[i]), cubePermutations)
		sys.exit(0)

