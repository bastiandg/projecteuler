#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Pandigital multiples

def concatMultiple(n, maxLen):
	string = ""
	i = 1
	while len(string) < maxLen:
		string += str(n*i)
		i += 1
	return string

def isPandigital(s):
	if len(s) != 9:
		return False
	for i in range(1,10):
		if str(i) not in s:
			return False
	return True

limit = 10000
max = "0"

for i in range(limit):
	conMul = concatMultiple(i, 9)
	if isPandigital(conMul):
		if conMul > max:
			print conMul
			max = conMul

