#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Title: Non-bouncy numbers

digits = 100
n100 = [i for i in range(10, 100)]
inc100 = [0] * 10
dec100 = [0] * 10

for i in n100:
	ones = i % 10
	tens = i // 10
	if tens > ones:
		dec100[ones] += 1
	else:
		inc100[ones] += 1

for i in range(1, 10):
	dec100[i] += 1  # adding 11 22 33 ...

incList = [[0] + [1] * 9, inc100]
decList = [[0] * 10, dec100]

for digit in range(digits - 2):
	countList = [0] * 10
	for i in range(10):
		countList[i] = sum(decList[-1][i:10])
	decList.append(countList)
	countList = [0] * 10
	for i in range(10):
		countList[i] = sum(incList[-1][0:i + 1])
	incList.append(countList)

nonBouncyCount = 0

for digitList in incList:
	nonBouncyCount += sum(digitList)
for digitList in decList:
	nonBouncyCount += sum(digitList)

nonBouncyCount -= (digits - 1) * 9  # subtract the falsely counted 11 222 333333 ...

print(nonBouncyCount)
