#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Minimal network

network = open("problem107.txt", "r").read().split("\n")[:-1]
edges = []

for i in range(len(network)):
	line = network[i]
	edgeStrings = line.split(",")
	for j in range(i, len(edgeStrings)):
		if edgeStrings[j] != "-":
			edges.append([int(edgeStrings[j]), i, j])

edges = sorted(edges)
minimalEdges = []

forests = []
for edge in edges:
	circle = False
	a = edge[1]
	b = edge[2]
	forestA = None
	forestB = None
	for i in range(len(forests)):
		forest = forests[i]
		if a in forest and b in forest:
			circle = True
			break
		elif a in forest:
			forestA = i
		elif b in forest:
			forestB = i
	if not circle:
		if forestA == None and forestB == None:
			forests.append(set([a, b]))
		elif forestA == None and forestB != None:
			forests[forestB].add(a)
		elif forestA != None and forestB == None:
			forests[forestA].add(b)
		else:
			forests[forestA].update(forests[forestB])
			del(forests[forestB])
		minimalEdges.append(edge)

edgeSum = 0
for edge in edges:
	edgeSum += edge[0]
minimalEdgeSum = 0
for edge in minimalEdges:
	minimalEdgeSum += edge[0]

print("%i - %i = %i" % (edgeSum, minimalEdgeSum, edgeSum - minimalEdgeSum))
