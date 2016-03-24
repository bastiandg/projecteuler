#!/usr/bin/env python3

from sympy import simplify

def lagrangePolynomial(pointList):
	function = ""
	for i in range(len(pointList)):
		term = "%i *" % pointList[i][1]
		for j in range(len(pointList)):
			if i != j:
				term += " ((x - %i) / (%i - %i)) *" % (pointList[j][0], pointList[i][0], pointList[j][0])
		function += "%s + " % term[:-2]
	return function[:-2]

pointList = []
approximationList = []

function = "1 - x + x**2 - x**3 + x**4 - x**5 + x**6 - x**7 + x**8 - x**9 + x**10"
# function = "x ** 3"
print("function: %s" % function)
print("")
function = str(simplify(function))
x = 1
while True:
	pointList.append([x, eval(function)])
	approximationList.append(str(simplify(lagrangePolynomial(pointList[:x + 1]))))
	x += 1
	if approximationList[-1] == function:
		break

bopSum = 0
for approximation in approximationList:
	print(approximation)
	for i in range(len(pointList)):
		x = pointList[i][0]
		y = eval(approximation)
		if [x, y] != pointList[i]:
			print("BOP: %i\n" % y)
			bopSum += y
			break
		elif i + 1 == len(pointList):
			print(80 * "-")
print(bopSum)
