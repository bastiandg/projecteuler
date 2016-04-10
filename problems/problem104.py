#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Pandigital Fibonacci ends

import math
import sys
from decimal import *

a = [0, 1]
digitCount = 9
pandigital = "123456789"
n = 100000
sqrt5 = Decimal(5).sqrt()
Phi = (Decimal(1) + sqrt5) / Decimal(2)
phi = (Decimal(1) - sqrt5) / Decimal(2)

def isPandigital(n):
	if n < 123456789:
		return False
	digits = set(range(1, 10))
	while n > 0:
		digit = n % 10
		if digit in digits:
			digits.remove(digit)
		else:
			return False
		n = n // 10
	return True

i = 1
while True:
	a[i % 2] = sum(a) % (10 ** digitCount)
	if a[i % 2] >= 123456789 and "".join(sorted(str(a[i % 2]))) == pandigital:
		f = (Phi ** Decimal(i) - phi ** Decimal(i)) / sqrt5
		p = "".join(sorted(str(f / Decimal(10 ** (int(f.log10()) - 8))).split(".")[0]))
		# print(f)
		# print(p)
		if p == pandigital:
			print("k: %i" % i)
			print(f)
			print(p)
			sys.exit(0)
	i += 1

