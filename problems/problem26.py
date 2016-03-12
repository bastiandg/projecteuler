#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Reciprocal cycles

def division(a,b):
	finished = False
	result = 0
	leadZero = 0
	remainderList = []
	periodLength = 0
	while True:
		d = int(a/b)
		result = result * 10 + d
		a -= d*b
		if result == 0 and d == 0:
			leadZero += 1
		a *= 10
		if a == 0:
			break
		elif a not in remainderList:
			remainderList.append(a)
		else:
			periodLength = len(remainderList) - remainderList.index(a)
			break
	return periodLength

limit = 1000
maxD = 0
maxPeriod = 0
for i in range(1,limit+1):
	length = division(1,i)
	if maxPeriod < length:
		maxPeriod = length
		maxD = i

print "%r: %r" % (maxD, maxPeriod)

