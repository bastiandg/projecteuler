#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Largest exponential
import math

exponentiationList = open("problem99.txt", "r").read().split("\n")[:-1]

# binary exponentiation
def power(x, n):
	if n == 0:
		return 1
	y = 1
	while n > 1:
		if n % 2 == 0:
			x *= x
			n = int(n / 2)
		else:
			y *= x
			x *= x
			n = int((n - 1) / 2)
	return x * y

maxPower = 0
maxIndex = 0

for i in range(len(exponentiationList)):
	x = int(exponentiationList[i].split(",")[0])
	n = int(exponentiationList[i].split(",")[1])
	xn = math.log(x) * n
	if xn > maxPower:
		maxPower = xn
		maxIndex = i + 1
		print(maxIndex)
