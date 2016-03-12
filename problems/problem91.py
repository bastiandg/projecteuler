#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Right triangles with integer coordinates
import math
import sys
import subprocess
import os
import itertools
from fractions import gcd

def primitivePythagoreanTriplet(max):
	tripletList = []
	for n in range(1, int(math.sqrt(max) + 1)):
		for m in range(n + 1, int(math.sqrt(max) + 1)):
			if gcd(n, m) == 1 and (m - n) % 2 == 1:
				a = m ** 2 - n ** 2
				b = 2 * m * n
				c = m ** 2 + n ** 2
				if c <= max:
					tripletList.append([a, b, c])
	return tripletList

def pythagoreanTriplet(max):
	primitiveList = primitivePythagoreanTriplet(max)
	tripletList = []
	for triplet in primitiveList:
		for i in range(1, int(max / triplet[2]) + 1):
			tripletList.append([triplet[0] * i, triplet[1] * i, triplet[2] * i])
	return tripletList

def execute(cmd):
	subprocess.call(cmd, shell=True)

def plot(v1, v2, v3):
	print(enum)
	plotfile = "/tmp/%i.plt" % enum
	f = open(plotfile, 'w')
	print("set terminal png size 400,400", file=f)
	print("set output '%i.png'" % enum, file=f)
	print("set object 1 poly from %i,%i to %i,%i to %i,%i to %i,%i fs empty border 1" % (v1[0], v1[1], v2[0], v2[1], v3[0], v3[1], v1[0], v1[1]), file=f)
	print("plot [0:4] [0:4] 0", file=f)
	f.close()
	execute("gnuplot %s" % plotfile)

def vectorAngle(v1, v2):
	a = (v1[0] * v2[0] + v1[1] * v2[1])
	b = (math.sqrt(v1[0] ** 2 + v1[1] ** 2) * math.sqrt(v2[0] ** 2 + v2[1] ** 2))
	c = a / b
	if c >= 1:
		return 0.0
	elif c <= -1:
		return 1.0
	return math.acos(c)


n = 50
vectorList = list(itertools.product(range(n + 1), repeat=2))[1:]
orthogonal = math.pi/2
orthogonalCount = 0

for i in range((n + 1) ** 2 - 1):
	x1 = vectorList[i][0]
	y1 = vectorList[i][1]
	for j in range(i + 1, (n + 1) ** 2 - 1):
		x2 = vectorList[j][0]
		y2 = vectorList[j][1]
		alpha = vectorAngle([x1, y1], [x2, y2])
		beta = vectorAngle([-x2, -y2], [x1 - x2, y1 - y2])
		gamma = vectorAngle([-x1, -y1], [x2 - x1, y2 - y1])
		if alpha == orthogonal or beta == orthogonal or gamma == orthogonal:
			orthogonalCount += 1
print(orthogonalCount)
