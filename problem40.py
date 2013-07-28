#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Champernowne's constant

string = ""
limit = 1000000
i = 1

while len(string) < limit:
	string += str(i)
	i += 1
print int(string[0])*int(string[10-1])*int(string[100-1])*int(string[1000-1])*int(string[10000-1])*int(string[100000-1])*int(string[1000000-1])
