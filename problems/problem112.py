#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Title: Bouncy numbers


def bouncy(n):
	digitList = []
	tmp = n
	down = False
	up = False
	digitList.append(tmp % 10)
	tmp = tmp // 10
	while tmp >= 1:
		digit = tmp % 10
		if digit > digitList[-1]:
			up = True
		elif digit < digitList[-1]:
			down = True
		digitList.append(digit)
		tmp = tmp // 10
	return up and down


ratio = 0.99
i = 0
bouncyCount = 0
while True:
	if bouncy(i):
		bouncyCount += 1
	if bouncyCount > 0 and bouncyCount / i == ratio:
		break
	if bouncyCount > 0 and i % 100 == 0:
		print(bouncyCount / i)
		# break
	i += 1

print("i %i bouncyCount %i" % (i, bouncyCount))
