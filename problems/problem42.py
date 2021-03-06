#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Coded triangle numbers

letterScores = dict({ "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26 })

f = open('words42.txt', 'r')
namesString = f.read()
names = namesString.replace('"','').split(",")
names = sorted(names)

triangleList = []
triangleWordCount = 0

tmp = 0
for i in range(1,50):
	tmp += i
	triangleList.append(tmp)

for i in range(len(names)):
	nameScore = 0
	for j in range(len(names[i])):
		nameScore += letterScores[names[i][j]]
	if nameScore in triangleList:
		triangleWordCount += 1

print triangleWordCount
