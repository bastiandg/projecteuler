#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Names scores

letterScores = dict({ "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26 })

f = open('names22.txt', 'r')
namesString = f.read()
names = namesString.replace('"','').split(",")
names = sorted(names)

scoreSum = 0

for i in range(len(names)):
	nameScore = 0
	for j in range(len(names[i])):
		nameScore += letterScores[names[i][j]]
	nameScore *= i+1
	scoreSum += nameScore

print scoreSum
