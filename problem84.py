#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Title: Monopoly odds

import random
import sys

def move(start, repeat):
	dice1 = random.randint(1, diceSides)
	dice2 = random.randint(1, diceSides)
	landingField = (start + dice1 + dice2) % boardSize
	if dice1 == dice2:
		if repeat == 2:
			landingField = 10
			repeat = 0
		else:
			repeat += 1
	else:
		repeat = 0
	landingField = action(landingField)
	return landingField, repeat

def action(landingField):
	# community chest
	if landingField in [2, 17, 33]:
		#print communityChestCards
		if communityChestCards[0] > 0:
			landingField = communityChestCards[0]
		communityChestCards.append(communityChestCards[0])
		del(communityChestCards[0])
	# chance
	elif landingField in [7, 22, 36]:
		if chanceCards[0] > 0:
			landingField = chanceCards[0]
		elif chanceCards[0] == -2:
			#there's no chance field before the first railway company
			if landingField == 7:
				landingField = 15
			elif landingField == 22:
				landingField = 25
			else:
				landingField = 5
		elif chanceCards[0] == -3:
			if landingField == 7:
				landingField = 12
			elif landingField == 22:
				landingField = 28
			else:
				landingField = 12
		elif chanceCards[0] == -4:
			landingField -= 3
			landingField = action(landingField)
		chanceCards.append(chanceCards[0])
		del(chanceCards[0])
	if landingField == 30:
		landingField = 10
	return landingField

def printBoard(board):
	row = ""
	for i in range(11):
		row += "%05d " % board[i]
	print row
	for i in range(9):
		print "%05d %s %05d" % (board[boardSize - i - 1], 53 * " ", board[11 + i])
	row = ""
	for i in range(11):
		row += "%05d " % board[30 - i]
	print row

# -1: nothing happens
# -2: move to the next railway company
# -3: move to the next utility company
# -4: go back 3 squares
# 0 - 39: move postition x
communityChestCards = 14 * [-1] + [0, 10]
random.shuffle(communityChestCards)
chanceCards = 6 * [-1] + [0, 10, 11, 24, 39, 5, -2, -2, -3, -4]
random.shuffle(chanceCards)

diceSides = 4
boardSize = 40
landingField = 0
repeat = 0
board = 40 * [0]

for i in range(100000):
	landingField, repeat = move(landingField, repeat)
	board[landingField] += 1

printBoard(board)

# dirty print, please ignore the following
max = 0
for i in range(boardSize):
	if board[i] > max:
		max = board[i]
		maxIndex = i
print maxIndex
board[maxIndex] = 0

max = 0
for i in range(boardSize - 1):
	if board[i] > max:
		max = board[i]
		maxIndex = i
print maxIndex
board[maxIndex] = 0

max = 0
for i in range(boardSize - 2):
	if board[i] > max:
		max = board[i]
		maxIndex = i
print maxIndex

