#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Triangular, pentagonal, and hexagonal
import sys
from sets import Set

pentagonSet = Set([])
triangleSet = Set([])
hexagonalSet = Set([])
limit = 100000

for i in range(1,limit+1):
	triangleSet.add(i*(i + 1)/2)

for i in range(1,limit+1):
	pentagonSet.add(i*(3*i - 1)/2)

for i in range(1,limit+1):
	hexagonalSet.add(i*(2*i - 1))

i1 = triangleSet.intersection(pentagonSet)
i2 = hexagonalSet.intersection(i1)

print i2

#print pentagonList

