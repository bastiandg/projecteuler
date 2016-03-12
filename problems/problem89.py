#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Roman numerals

digits = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
brokenDigits = { "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
compoundList = { 1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M" }

def value(numeral):
	value = 0
	for brokenDigit in brokenDigits.keys():
		while True:
			if numeral != numeral.replace(brokenDigit, "", 1):
				value += brokenDigits[brokenDigit]
				numeral = numeral.replace(brokenDigit, "", 1)
			else:
				break
	for digit in digits.keys():
		while True:
			if numeral != numeral.replace(digit, "", 1):
				value += digits[digit]
				numeral = numeral.replace(digit, "", 1)
			else:
				break
	return value

def numeral(n):
	numeral = ""
	for compound in sorted(compoundList.keys(), reverse=True):
		while True:
			if n >= compound:
				numeral += compoundList[compound]
				n -= compound
			else:
				break
	return numeral

numeralList = open("problem89.txt", "r").read().split("\n")[:-1]

savings = 0
for num in numeralList:
	savings += len(num) - len(numeral(value(num)))

print savings
