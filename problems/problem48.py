#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Self powers

limit = 1000
selfPowerSum = 0

for i in range(1, limit+1):
	selfPowerSum += i**i
print selfPowerSum

