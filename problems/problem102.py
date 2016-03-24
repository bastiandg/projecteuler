#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Triangle containment

def orientation(a, b, c):
	return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - a[0] * c[1] - b[0] * a[1] - c[0] * b[1]

def orientation0(a, b):
	return a[0] * b[1] - b[0] * a[1]

containmentCount = 0

triangleList = open("problem102.txt", "r").read().split("\n")[:-1]
for triangle in triangleList:
	pointList = triangle.split(",")
	a = (int(pointList[0]), int(pointList[1]))
	b = (int(pointList[2]), int(pointList[3]))
	c = (int(pointList[4]), int(pointList[5]))
	o1 = orientation0(a, b)
	o2 = orientation0(b, c)
	o3 = orientation0(c, a)
	if o1 >= 0 and o2 >= 0 and o3 >= 0:
		containmentCount += 1
	elif o1 <= 0 and o2 <= 0 and o3 <= 0:
		containmentCount += 1

print(containmentCount)
