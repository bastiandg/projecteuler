#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Factorial digit sum

import math

def digitSum(n, base):
	dSum = 0
	while n >= 1:
		dSum += n % base
		n /= base
	return dSum

print digitSum(math.factorial(100),10)
#print math.factorial(100)
