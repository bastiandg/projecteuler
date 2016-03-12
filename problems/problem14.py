#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Longest Collatz sequence

def collatz(n):
	steps = 0
	#string = ""
	while n != 1:
		steps += 1
		#string += "%r -> " % n
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n+1
	#print "%s 1" % string
	return steps+1

maxSteps = 0
maxStepsNum = 0
for i in range(1,1000000):
	steps = collatz(i)
	if steps > maxSteps:
		maxSteps = steps
		maxStepsNum = i
		print "%r has %r steps" % (maxStepsNum, maxSteps)


