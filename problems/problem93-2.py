#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Arithmetic expressions

import itertools

expressionList = open("expression93.list", "r").read().split("\n")[:-1]

max = 0
for vset in itertools.combinations(range(1, 10), 4):
	a = vset[0]
	b = vset[1]
	c = vset[2]
	d = vset[3]
	resultSet = set()
	for expression in expressionList:
		try:
			result = eval(expression)
			if result == int(result):
				resultSet.add(int(result))
		except ZeroDivisionError:
			pass
	for i in range(1, 1500):
		if i not in resultSet:
			break
	if max < i:
		max = i - 1
		maxSet = [a, b, c, d]
		print(maxSet)

print(max)
print(maxSet)
