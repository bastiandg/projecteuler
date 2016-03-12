#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Counting summations

import math
import numpy


def f(l, N):
	a = [1]+[0]*N
	for i in l:
		for j in range(N-i+1):
			a[i+j] += a[j]
	return a[-1]

#target = 100000
#table = [1] + [0] * target
#for value in xrange(1, target):
	##print value
	#for i in xrange(value, target+1):
		#table[i] += table[i-value]
		##table[i] = table[i] % n
	#if table[value] % n == 0:
		##print "AAAAAAAAAAAAAAA"
		#print "%i %i" % (value, table[value])
	#if value % 100 == 0:
		#print value
#print table

p_memo = {}
def p(n):
	if n in p_memo:
		return p_memo[n]
	elif n == 0:
		return 1
	elif n < 0:
		return 0
	p_memo[n] = 0
	count = 1
	while True:
		term = 0
		for k in [count, -count]:
			term = int((-1) ** (k - 1)) * p(n - (k*(3*k-1))/2)
			p_memo[n] += term
		if term == 0:
			break
		count += 1
	return p_memo[n]

n = 1000000
limit = 100000

for i in xrange(0, limit):
	if p(i) % n == 0:
		print i
