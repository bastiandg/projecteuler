#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Digit fifth powers

digits = 5
limit = 413343
powerSum = 0

def digitPowerSum(n):
	tmp = n
	dpSum = 0
	while tmp >= 1:
		dpSum += (tmp%10)**digits
		tmp /= 10
	return dpSum

for i in range(2, limit):
	if digitPowerSum(i) == i:
		print i
		powerSum += i
print powerSum
