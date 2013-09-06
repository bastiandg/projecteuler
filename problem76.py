#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Counting summations

import math

comboList = dict()
alphabet = range(1, 1001)
def concat(a, b):
	return int(a * 10 ** math.ceil(math.log10(b)) + b)

def split(n, min=1, tab=6):
	#print "%sn = %i, min = %i" % ("	"*tab, n, min)
	if concat(n,min) in comboList.keys():
		return comboList[concat(n,min)]
	if int(n) < int(min + 1):
		#print "KJLJKLJ"
		return 1
	splitSum = 0
	splitList = []
	for i in range(len(alphabet)):
		if alphabet[i] > n/2:
			break
		if (n - alphabet[i]) in alphabet and not alphabet[i] < min:
			splitSum += split(n - alphabet[i], alphabet[i], tab - 1)
			#splitList.append((n - alphabet[i], alphabet[i]))
	#for s in splitList:
	comboList[concat(n,min)] = splitSum + 1
	return splitSum + 1
	#return splitList

print split(120) - 1
print len(comboList)
#print split(7)
