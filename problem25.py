#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: 1000-digit Fibonacci number
import math

limit = 1000
f1 = 1
f2 = 1
i = 2

while math.log10(f2) < (limit-1):
	tmp = f2
	f2 = f1 + f2
	f1 = tmp
	i += 1

print f1
print f2
print i
