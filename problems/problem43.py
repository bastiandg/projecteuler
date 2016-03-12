#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Sub-string divisibility

mul2 = []
mul3 = []
mul5 = []
mul7 = []
mul11 = []
mul13 = []
mul17 = []
numbers = [0,1,2,3,4,5,6,7,8,9]

def digits(n):
	digitList = []
	tmp = n
	while tmp >= 1:
		digitList.insert(0,tmp%10)
		tmp /= 10
	if n < 100:
		digitList.insert(0,0)
		if n < 10:
			digitList.insert(0,0)
	return digitList


def multiples(n):
	multipleList = []
	for i in range(1,1000/n+1):
		digitList = digits(n*i)
		if len(digitList) == len(set(digitList)):
			multipleList.append(digitList)
	return multipleList

def concat(l2, l1):
	l = list(l1)
	if l2[1] == l1[0] and l2[2] == l1[1]:
		l.insert(0,l2[0])
		if len(l) == len(set(l)):
			return l
		else:
			return None
	else:
		return None

mul17 = multiples(17)
mul13 = multiples(13)
mul11 = multiples(11)
mul7 = multiples(7)
mul5 = multiples(5)
mul3 = multiples(3)
mul2 = multiples(2)

superSum = 0
for i1 in mul17:
	for i2 in mul13:
		num1 = concat(i2, i1)
		if num1:
			for i3 in mul11:
				num2 = concat(i3, num1)
				if num2:
					for i4 in mul7:
						num3 = concat(i4, num2)
						if num3:
							for i5 in mul5:
								num4 = concat(i5, num3)
								if num4:
									for i6 in mul3:
										num5 = concat(i6, num4)
										if num5:
											for i7 in mul2:
												num6 = concat(i7, num5)
												if num6:
													nums = list(numbers)
													pandigitalNum = 0
													for i in range(len(num6)):
														pandigitalNum += 10**(9-i-1) * num6[i]
														nums.remove(num6[i])
													pandigitalNum += nums[0] * 10**9
													superSum += pandigitalNum
													print pandigitalNum

print superSum
