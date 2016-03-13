#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Square digit chains

loop = set([89, 145, 42, 20, 4, 16, 37, 58])
end = set([100, 10, 1])
loopCount = 0

def digitSquareSum(n):
	s = 0
	while n > 0:
		s += (n % 10) ** 2
		n = int(n / 10)
	return s

for i in range(1, 10 ** 7):
	chain = [i]
	tmp = i
	while True:
		if tmp in loop:
			for t in chain:
				loop.add(t)
			loopCount += 1
			break
		elif tmp in end:
			for t in chain:
				end.add(t)
			break
		tmp = digitSquareSum(tmp)
		chain.append(tmp)
print(loopCount)
