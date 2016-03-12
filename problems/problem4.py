#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Largest palindrome product

def isPalindrom(n):
	string = str(n)
	if string == string[::-1]:
		return True
	else:
		return False

start = 100
limit = 999
max = 0
f1 = start
f2 = start

for i in range(start,limit):
	for j in range(start,limit):
		product = i * j
		if isPalindrom(product) and product > max:
			max = product
			maxI = i
			maxJ = j
			print max

print "%r * %r = %r" % (maxI, maxJ, max)
