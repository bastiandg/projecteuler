#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Coin sums

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
possibilities = 0

for i7 in range(int(amount/coins[7])+1):
	sum7 = amount-i7*coins[7]
	for i6 in range(int(sum7/coins[6])+1):
		sum6 = sum7-i6*coins[6]
		for i5 in range(int(sum6/coins[5])+1):
			sum5 = sum6-i5*coins[5]
			for i4 in range(int(sum5/coins[4])+1):
				sum4 = sum5-i4*coins[4]
				for i3 in range(int(sum4/coins[3])+1):
					sum3 = sum4-i3*coins[3]
					for i2 in range(int(sum3/coins[2])+1):
						sum2 = sum3 - i2*coins[2]
						for i1 in range(int(sum2/coins[1])+1):
							sum1 = sum2 - i1*coins[1]
							possibilities += 1

print possibilities
