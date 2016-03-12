#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Multiples of 3 and 5

limit = 1000
s = 0
for i in range(1,limit):
	if i % 3 == 0 or i % 5 == 0:
		s += i
print s
