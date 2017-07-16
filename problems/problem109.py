#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Title: Darts

import itertools


def points(turn):
	pointSum = 0
	for throw in turn:
		pointSum += regions[throw]
	return pointSum


regions = {}

for i in range(1, 21):
	regions["S%i" % i] = i
for i in range(1, 21):
	regions["D%i" % i] = i * 2
for i in range(1, 21):
	regions["T%i" % i] = i * 3
regions["B1"] = 50
regions["B2"] = 25

turns = []

prethrows = list(itertools.combinations_with_replacement(regions.keys(), 2))

for region in regions.keys():
	for prethrow in prethrows:
		turns.append(prethrow + (region,))

for region in regions.keys():
	for region2 in regions.keys():
		turns.append((region, region2))

for region in regions.keys():
	turns.append((region,))

endings = []
smallEndings = 0
for turn in turns:
	lastMove = turn[-1]
	if lastMove[0] == "D" or lastMove == "B1":
		endings.append(turn)
		if points(turn) < 100:
			smallEndings += 1


print(len(endings))
print(smallEndings)
