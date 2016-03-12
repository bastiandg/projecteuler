#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Sum square difference
limit = 100
squareSum = 0
sumSquare = 0
for i in range(limit+1):
	squareSum += i**2
	sumSquare += i
sumSquare = sumSquare ** 2
print sumSquare
print squareSum
print sumSquare - squareSum
