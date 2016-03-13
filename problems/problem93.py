#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Title: Arithmetic expressions

import itertools
from sympy import simplify

baseExpressions = [ "S1 A O1 S2 B O2 S3 C O3 S4 D",
                    "(S1 A O1 S2 B) O2 S3 C O3 S4 D",
                    "S1 A O1 (S2 B O2 S3 C) O3 S4 D",
                    "S1 A O1 S2 B O2 (S3 C O3 S4 D)",
                    "(S1 A O1 S2 B O2 S3 C) O3 S4 D",
                    "S1 A O1 (S2 B O2 S3 C O3 S4 D)",
                    "(S1 A O1 S2 B) O2 (S3 C O3 S4 D)",
                    "((S1 A O1 S2 B) O2 S3 C) O3 S4 D"]

expressions = set()
simplifiedExpressions = set()

operators = ["+", "-", "*", "/"]
it = 0

for baseExpression in baseExpressions:
	for signs in itertools.product(operators[:2], repeat=4):
		bex = baseExpression
		bex = bex.replace("S1", signs[0])
		bex = bex.replace("S2", signs[1])
		bex = bex.replace("S3", signs[2])
		bex = bex.replace("S4", signs[3])
		for ops in itertools.product(operators, repeat=3):
			it += 1
			be = bex
			be = be.replace("O1", ops[0])
			be = be.replace("O2", ops[1])
			be = be.replace("O3", ops[2])
			expressions.add(be.replace("+ +", "+").replace("- -", "+").replace("- +", "-").replace("* +", "*").replace("/ +", "/").replace("+ -", "-"))

for expression in expressions:
	simplifiedExpressions.add(str(simplify(expression)))

variables = ["a", "b", "c", "d"]
allExpressions = set()
for simplifiedExpression in simplifiedExpressions:
	for v in itertools.permutations(variables):
		se = simplifiedExpression
		se = se.replace("A", v[0])
		se = se.replace("B", v[1])
		se = se.replace("C", v[2])
		se = se.replace("D", v[3])
		allExpressions.add(str(simplify(se)))

for expression in allExpressions:
	print(expression)
