#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Number letter counts

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numberString(n):
	string = ""
	rem = n%100
	if rem < 10:
		string = ones[int(n%10)]
	elif rem == 10:
		string = "ten"
	elif rem == 11:
		string = "eleven"
	elif rem == 12:
		string = "twelve"
	elif rem == 13:
		string = "thirteen"
	elif rem == 15:
		string = "fifteen"
	elif rem == 18:
		string = "eighteen"
	elif rem in [14,16,17,19]:
		string = "%steen" %  ones[int(n%10)]
	else:
		string = "%s%s" % (tens[int((n%100)/10 - 2)], ones[int(n%10)])

	hundreds = int(n/100)
	if hundreds >= 1 and rem == 0:
		string = "%shundred" % (ones[int(hundreds)])
	elif hundreds >= 1:
		string = "%shundredand%s" % (ones[int(hundreds)], string)
	print string
	return len(string)

#print numberString(299)
letterSum = 0
for i in range(1,1000):
	l = numberString(i)
	print l
	letterSum += l
letterSum += len("onethousand")
print letterSum
