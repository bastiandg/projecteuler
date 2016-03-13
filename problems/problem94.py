#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Almost equilateral triangles

import math
from decimal import *
from fractions import gcd

perimeterSum = 0
max = 10 ** 9
complete = int((math.sqrt(max / 3 + 1) + 1))
for n in range(1, int((math.sqrt(max / 3 + 1) + 1))):
	if n % 100 == 0:
		print(n / complete)
	for m in range(n + 1, int((math.sqrt(max / 3 + 1) + 1))):
		if (n - m) % 2 == 1 and gcd(n, m) == 1 and (m - n) % 2 == 1:
			n2 = n ** 2
			m2 = m ** 2
			a = m2 - n2
			b = 2 * m * n
			c = m2 + n2
			x = min(a, b) * 2
			if c <= max:
				if c == x + 1:
					perimeterSum += x * 3 + 2
				elif c == x - 1:
					perimeterSum += x * 3 - 2

print(perimeterSum)
