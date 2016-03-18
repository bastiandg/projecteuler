#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Arranged probability

import math
import sys
from gmpy2 import is_square
from decimal import *

n = 10 ** 12
accuracyRange = 0.1
bi = 15
factor = Decimal(1154) ** Decimal(1.0 / 4.0)

while True:
	guess = int(Decimal(bi) * factor)
	for i in range(int(guess * (1 - accuracyRange)), int(guess * (1 + accuracyRange))):
		c = 2 * i * (i - 1)
		square = c + int(math.sqrt(c) + 1)
		if is_square(square):
			x = math.sqrt(2 * i * (i - 1) + 1/4) + 1/2
			accuracyRange = abs(float(Decimal(i - guess)/ Decimal(i)))
			if x > n:
				print(i)
				sys.exit(0)
			bi = i
			break
