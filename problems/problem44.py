#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Pentagon numbers
import sys

pentagonList = []
limit = 10000

for i in range(1,limit+1):
	pentagonList.append(i*(3*i - 1)/2)
	#print i*(3*i - 1)/2

#print pentagonList

for p1 in pentagonList:
	print "%r" % ((float(pentagonList.index(p1))/float(limit))*100.0)
	for p2 in pentagonList:
		if p1 <= p2 or (p1 + p2) > pentagonList[-1]:
			break
		if (p1 - p2) in pentagonList and (p1 + p2) in pentagonList:
			print "%r - %r = %r" % (p1, p2, p1 - p2)
			print "%r + %r = %r" % (p1, p2, p1 + p2)
			sys.exit(0)
