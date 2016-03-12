#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Cuboid route

import math

max = 100
cuboidList = set()
cuboidList2 = set()

def isInt(n):
	if int(n) == n:
		return True
	else:
		return False

def intCuboid(a, b, c):
	path1 = math.sqrt((a + b) ** 2 + c**2)
	path2 = math.sqrt((a + c) ** 2 + b**2)
	path3 = math.sqrt((b + c) ** 2 + a**2)
	return isInt(min(path1, path2, path3))

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

#u = 1
#i = 0

#while True:
	#for v in range(1, u):
		##if (u + v) % 2 == 1:
		#x = u * u - v * v
		#y = 2 * u * v
		#z = u * u + v * v
		##print "%i, %i: %i^2 + %i^2 = %i^2" % (u, v, x, y, z)
		#for j in range(1, y / 2):
			#if x <= M and y - j <= M and j <= M:
				##if j == 8:
					##print tuple(sorted((x, y - j, j)))
				#cuboidList.add(tuple(sorted((x, y - j, j))))
		#for j in range(1, x / 2):
			#if y <= M and x - j <= M and j <= M:
				##if j == 8:
					##print tuple(sorted((y, x - j, j)))
				#cuboidList.add(tuple(sorted((y, x - j, j))))
		#i += 1
		#if i == max:
			#break
	#if i == max:
		#break
	#u += 1

i = 1
l = 10000
while True:
	#for i in range(1, max + 1):
	for j in range(1, i + 1):
		for k in range(1, j + 1):
			if intCuboid(i, j, k):
				cuboidList2.add(tuple((k, j, i)))
	if len(cuboidList2) >= l:
		l += 10000
		print len(cuboidList2)
		print i
	if len(cuboidList2) >= 1000000:
		print i
		break
	i += 1

print len(cuboidList2)

