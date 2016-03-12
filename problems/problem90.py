#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Cube digit pairs

import itertools

conditionList = { 0: [1, 4, 9], 1: [0, 6, 8], 2: [5], 3: [6], 4: [6, 9], 5: [2] }

def validDiceCombination(a, b):
	if a == b:
		return False
	ab = a + b

	for i in [0, 1, 2, 3, 4, 5, 6, 8, 9]:
		if i not in ab:
			return False

	for key in conditionList.keys():
		if key in a and key in b:
			tmp = a + b
		elif key in a:
			tmp = b
		else:
			tmp = a
		for i in conditionList[key]:
			if i not in tmp:
				return False
	return True

alphabet = range(10)
diceList = []
for dice in itertools.combinations(alphabet, 6):
	if 6 in dice and 9 not in dice:
		diceList.append(dice + tuple([9]))
	elif 9 in dice and 6 not in dice:
		diceList.append(dice + tuple([6]))
	else:
		diceList.append(dice)

solutions = 0
for i in range(len(diceList)):
	for j in range(i, len(diceList)):
		if validDiceCombination(diceList[i], diceList[j]):
			solutions += 1
print(solutions)
