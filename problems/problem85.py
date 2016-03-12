#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Counting rectangles

gridMaxSize = 100

rectangleCount = 0
approximatedCount = 2 * 10**6
bestApproximationDifference = 10**9
bestApproximationArea = 0


for gridHeight in range(1, gridMaxSize + 1):
	for gridWidth in range(1, gridMaxSize + 1):
		for i in range(1, gridHeight + 1):
			for j in range(1, gridWidth + 1):
				rectangleCount += (gridHeight - i + 1) * (gridWidth - j + 1)
		if abs(rectangleCount - approximatedCount) < bestApproximationDifference:
			bestApproximationDifference = abs(rectangleCount - approximatedCount)
			bestApproximationArea = gridHeight * gridWidth
		rectangleCount = 0

print bestApproximationDifference
print bestApproximationArea

