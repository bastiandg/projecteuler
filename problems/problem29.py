#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Distinct powers

powerList = []
limit = 100

for i in range(2,limit+1):
	for j in range(2,limit+1):
		powerList.append(j**i)
		powerList.append(i**j)

powerList = set(powerList)
print len(powerList)
