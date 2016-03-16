#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Su Doku
import sys
import copy

class Sudoku():
	"""sudoku class"""
	def __init__(self, numbers, possibilityList=None):
		self.numbers = numbers
		self.possibilityList = possibilityList
		if possibilityList == None:
			self.possibilityList = [[[] for x in range(9)] for x in range(9)]
			self.possibilities()

	def possibilities(self):
		for x in range(9):
			for y in range(9):
				if self.numbers[x][y] != 0:
					self.possibilityList[x][y] = []
				else:
					cellPossibilityList = range(1, 10)
					section = (x // 3, y // 3)
					# test section
					for i in range(section[0] * 3, section[0] * 3 + 3):
						for j in range(section[1] * 3, section[1] * 3 + 3):
							if self.numbers[i][j] != 0 and self.numbers[i][j] in cellPossibilityList:
								cellPossibilityList.remove(self.numbers[i][j])
					# test line
					for i in range(9):
						if self.numbers[x][i] != 0 and self.numbers[x][i] in cellPossibilityList:
							cellPossibilityList.remove(self.numbers[x][i])
					# test column
					for i in range(9):
						if self.numbers[i][y] != 0 and self.numbers[i][y] in cellPossibilityList:
							cellPossibilityList.remove(self.numbers[i][y])
					self.possibilityList[x][y] = cellPossibilityList

	def solveEasy(self):
		for x in range(9):
			for y in range(9):
				if len(self.possibilityList[x][y]) == 1:
					self.numbers[x][y] = self.possibilityList[x][y][0]
					self.possibilities()
					self.solveEasy()
					return

	def solveMedium(self):
		for x in range(9):
			openNumbers = dict()
			for y in range(9):
				for p in self.possibilityList[x][y]:
					if p not in openNumbers.keys():
						openNumbers[p] = [y]
					else:
						openNumbers[p] += [y]
			for p in openNumbers.keys():
				if len(openNumbers[p]) == 1:
					self.numbers[x][openNumbers[p][0]] = p
					self.possibilities()
					self.solveEasy()
					self.solveMedium()
					return
		for y in range(9):
			openNumbers = dict()
			for x in range(9):
				for p in self.possibilityList[x][y]:
					if p not in openNumbers.keys():
						openNumbers[p] = [x]
					else:
						openNumbers[p] += [x]
			for p in openNumbers.keys():
				if len(openNumbers[p]) == 1:
					self.numbers[openNumbers[p][0]][y] = p
					self.possibilities()
					self.solveEasy()
					self.solveMedium()
					return
			for i in range(3):
				for j in range(3):
					openNumbers = dict()
					for x in range(i * 3, i * 3 + 3):
						for y in range(j * 3, j * 3 + 3):
							for p in self.possibilityList[x][y]:
								if p not in openNumbers.keys():
									openNumbers[p] = [[x, y]]
								else:
									openNumbers[p] += [[x, y]]
					for p in openNumbers.keys():
						if len(openNumbers[p]) == 1:
							self.numbers[openNumbers[p][0][0]][openNumbers[p][0][1]] = p
							self.possibilities()
							self.solveEasy()
							self.solveMedium()
							return
	def solveHard(self):
		minPossibilities = 10
		for x in range(9):
			for y in range(9):
				if self.possibilityList[x][y] != [] and len(self.possibilityList[x][y]) < minPossibilities:
					minPossibilities = len(self.possibilityList[x][y])
					minIndex = [x, y]
		if minPossibilities == 10:
			return
		x = minIndex[0]
		y = minIndex[1]
		for p in self.possibilityList[x][y]:
			tmpNumbers = copy.deepcopy(self.numbers)
			tmpPossibilityList = copy.deepcopy(self.possibilityList)
			tmpNumbers[x][y] = p
			tmpPossibilityList[x][y] = []
			s = Sudoku(tmpNumbers, tmpPossibilityList)
			s.solve()
			if s.isComplete():
				self.numbers = copy.deepcopy(s.numbers)
				self.possibilityList = copy.deepcopy(s.possibilityList)
				return

	def solve(self):
		self.possibilities()
		self.solveEasy()
		self.solveMedium()
		self.solveHard()

	def display(self):
		for i in range(9):
			line = ""
			for j in range(9):
				line += "%i " % self.numbers[i][j]
				if j % 3 == 2:
					line += " "
			if i % 3 == 2:
				line += "\n"
			print(line)

	def isValid(self):
		for i in range(9):
			line = sorted(self.numbers[i])
			for j in range(8):
				if line[j] != 0 and line[j] == line[j + 1]:
					return False
		for i in range(9):
			column = [self.numbers[j][i] for j in range(9)]
			for j in range(8):
				if column[j] != 0 and column[j] == column[j + 1]:
					return False
		for i in range(3):
			for j in range(3):
				section = []
				for k in range(i * 3, i * 3 + 3):
					for l in range(j * 3, j * 3 + 3):
						section.append(self.numbers[k][l])
				for j in range(8):
					if section[j] != 0 and section[j] == section[j + 1]:
						return False
		return True

	def isComplete(self):
		for i in range(9):
			if sorted(self.numbers[i]) != range(1, 10):
				return False
		for i in range(9):
			if sorted([self.numbers[j][i] for j in range(9)]) != range(1, 10):
				return False
		for i in range(3):
			for j in range(3):
				section = []
				for k in range(i * 3, i * 3 + 3):
					for l in range(j * 3, j * 3 + 3):
						section.append(self.numbers[k][l])
				if sorted(section) != range(1, 10):
					return False
		return True

	def topLeftCorner(self):
		return self.numbers[0][0] * 100 + self.numbers[0][1] * 10 + self.numbers[0][2]

sudokuFilePath = "problem96.txt"
sudokuFile = open(sudokuFilePath, "r").read().split("\n")[:-1]
topLeftCornerSum = 0

for i in range(50):
	tmp = sudokuFile[i * 10 + 1:(i + 1) * 10]
	numbers = []
	for line in tmp:
		l = []
		for field in line:
			number = int(field)
			l.append(number)
		numbers.append(l)
	possibilityList = {}
	s = Sudoku(numbers)
	s.solve()
	if not s.isComplete():
		sys.exit(9)
	topLeftCornerSum += s.topLeftCorner()

print(topLeftCornerSum)
