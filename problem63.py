#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Powerful digit counts

import math

counter = 0

for i in range(1,10):
	for j in range(1,22):
		if int(math.floor(math.log10(i ** j) + 1)) == j:
			counter += 1

print counter
