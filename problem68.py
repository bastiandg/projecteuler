#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Magic 5-gon ring

import itertools

def concat(list):
	string = ""
	index = ((5, 0, 1), (6, 1, 2), (7, 2, 3), (8, 3, 4), (9, 4, 0))
	start = list.index(min(list[5:]))
	for i in range(start, start + 5):
		for j in (0, 1, 2):
			string += str(p[index[(i - 5) % 5][j]])
	return string
	#return str(p[5]) + str(p[0]) + str(p[1]) + str(p[6]) + str(p[1]) + str(p[2]) + str(p[7]) + str(p[2]) + str(p[3]) + str(p[8]) + str(p[3]) + str(p[4]) + str(p[9]) + str(p[4]) + str(p[0])

solution = []
solution2 = []
for p in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)):
	s = p[5] + p[0] + p[1]
	if s == p[6] + p[1] + p[2] and \
		s == p[7] + p[2] + p[3] and \
		s == p[8] + p[3] + p[4] and \
		s == p[9] + p[4] + p[0]:
		if len(concat(p)) == 16:
			solution.append(int(concat(p)))
			print p
			print concat(p)
		solution2.append(int(concat(p)))

print sorted(solution2)
print "MAX: %i" % max(solution)
