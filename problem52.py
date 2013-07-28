#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Permuted multiples

import sys
import math

def digits(n):
	digitList = []
	tmp = n
	while tmp >= 1:
		digitList.append(tmp%10)
		tmp /= 10
	return sorted(digitList)

limit = 1000000
for i in range(limit):
	if digits(i) == digits(i*2) == digits(i*3) == digits(i*4) == digits(i*5) == digits(i*6):
		print i
