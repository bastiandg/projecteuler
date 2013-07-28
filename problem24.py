#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Lexicographic permutations
import math

characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation = []
index = 1000000
index -=1
tmpCharacters = list(characters)
tmpIndex = index

for i in range(len(characters)):
	d = int(tmpIndex/math.factorial(len(characters)-(i+1)))
	permutation.append(tmpCharacters[d])
	tmpCharacters.pop(d)
	tmpIndex = tmpIndex - d*(math.factorial(len(characters)-(i+1)))

string = ""
for c in permutation:
	string += str(c)
print string
