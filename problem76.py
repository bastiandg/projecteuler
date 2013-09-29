#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Counting summations

import math

limit = 201
comboList = dict()
alphabet = range(1, limit)
searchAlphabet = set(alphabet)
def concat(a, b):
	return "%i %i" % (a, b)

def split(n, min=1, tab=6):
	if concat(n,min) in comboList.keys():
		if tab == 6:
			print " %sn = %i, min = %i, %i" % ("	"*tab, n, min, concat(n, min))
		return comboList[concat(n,min)]
	if int(n) < int(min + 1):
		return 1
	splitSum = 0
	splitList = []
	for i in range(len(alphabet)):
		if alphabet[i] > n/2:
			break
		if (n - alphabet[i]) in alphabet and not alphabet[i] < min:
			splitSum += split(n - alphabet[i], alphabet[i], tab - 1)
	comboList[concat(n,min)] = splitSum + 1
	return splitSum + 1

#print split(99) -1
#print split(100) -1
splits = []
for i in range(limit):
	splits.append(split(i) - 1)
	print "%i: %i" % (i, splits[i])

