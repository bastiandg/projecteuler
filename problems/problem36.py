#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Double-base palindromes

digitStrings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def baseString(number, base):
	string = ""
	while number:
		string = digitStrings[number % base] + string
		number /= base
	return string

def isPalindrom(n, base):
	string = baseString(n, base)
	if string == string[::-1]:
		return True
	else:
		return False

limit = 1000000
doublePalindromSum = 0

for i in range(1, limit):
	if isPalindrom(i, 10) and isPalindrom(i, 2):
		doublePalindromSum += i

print doublePalindromSum
