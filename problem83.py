#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Title: Path sum: two ways

import sys
limit = 10

path = "problem81.txt"
matrixString = open(path, "r").read().split("\n")[:-1]
matrix = []
matrixPathSum = []
matrixVisited = []
c = 0
checkList = set()

def display(m):
	countY = 0
	for line in m:
		if countY < limit:
			printLine = ""
			countX = 0
			for value in line:
				printLine += "%05d " % value
				countX += 1
				if countX == limit:
					break
			print(printLine)
		countY += 1

def minimum():
	min = float("inf")
	minX = -1
	minY = -1
	minIndex = -1
	for point in checkList:
			if not matrixVisited[point[0]][point[1]] and matrixPathSum[point[0]][point[1]] < min:
				min = matrixPathSum[point[0]][point[1]]
				minX = point[0]
				minY = point[1]
	if minY != -1:
		checkList.remove((minX, minY))
	return minX, minY

def way(x, y):
	global c
	c += 1
	if c % 1000 == 0:
		print(c)
	if matrixVisited[x][y]:
		return
	successorList = []
	if y > 0:
		successorList.append((x, y - 1))
		if not matrixVisited[x][y - 1]:
			checkList.add((x, y - 1))
	if x > 0:
		successorList.append((x - 1, y))
		if not matrixVisited[x - 1][y]:
			checkList.add((x - 1, y))
	if x < len(matrix) - 1:
		successorList.append((x + 1, y))
		if not matrixVisited[x + 1][y]:
			checkList.add((x + 1, y))
	if y < len(matrix[0]) - 1:
		successorList.append((x, y + 1))
		if not matrixVisited[x][y + 1]:
			checkList.add((x, y + 1))
	for successor in successorList:
		if (matrixPathSum[x][y] + matrix[successor[0]][successor[1]]) < matrixPathSum[successor[0]][successor[1]]:
			matrixPathSum[successor[0]][successor[1]] = matrixPathSum[x][y] + matrix[successor[0]][successor[1]]
	matrixVisited[x][y] = True


for line in matrixString:
	values = [int(n) for n in line.split(",")]
	matrix.append(values)
	matrixPathSum.append([float("inf")] * len(values))
	matrixVisited.append([False] * len(values))

#for i in range(len(matrix)):
	#matrixPathSum[i][0] = matrix[i][0]
	#checkList.add((i,0))
checkList.add((0,0))

matrixPathSum[0][0] = matrix[0][0]
display(matrix)

while True:
	x, y = minimum()
	if x == -1:
		break
	way(x, y)

min = float("inf")
for line in matrixPathSum:
	if line[-1] < min:
		min = line[-1]

print(min)

display(matrixPathSum)
print(matrixPathSum[79][79])
