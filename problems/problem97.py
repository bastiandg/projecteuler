#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Large non-Mersenne prime

factor = 28433
power = 7830457
constant = 1
digits = 10

result = 1

for i in range(power):
	result = result << 1
	result = result % (10 ** (digits))

result *= factor
result += constant
result = result % (10 ** digits)
print(result)

