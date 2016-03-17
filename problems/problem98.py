#!/usr/bin/env python3
import math
import sys

wordList = open("problem98.txt", "r").read().replace("\"", "").split(",")

wordList[-1] = wordList[-1].replace("\n", "")
anagramDict = dict()
maxLen = 0
maxIndex = 0

# anagram mapping
for i in range(len(wordList)):
	for j in range(i + 1, len(wordList)):
		if sorted(wordList[i]) == sorted(wordList[j]):
			if len(wordList[i]) in anagramDict.keys():
				anagramDict[len(wordList[i])] += [[wordList[i], wordList[j]]]
			else:
				anagramDict[len(wordList[i])] = [[wordList[i], wordList[j]]]

anagramSquareList = []
for length in sorted(anagramDict.keys(), reverse=True):
	upperBound = (10 ** length) - 1
	lowerBound = 10 ** (length - 1)
	start = int(math.sqrt(lowerBound))
	stop = int(math.sqrt(upperBound) + 1)
	tmpSquare = start ** 2
	squareSet = set(str(tmpSquare))

	for i in range(start + 1, stop):
		tmpSquare += i + i - 1
		squareSet.add(str(tmpSquare))

	for anagramPair in anagramDict[length]:
		word = anagramPair[0]
		anagram = anagramPair[1]
		uniqueCount = len(set(word))
		tmpSquareSet = set(squareSet)
		repeatedCharacters = []
		for i in range(len(word) - 1):
			for j in range(i + 1, len(word)):
				if word[i] == word[j]:
					repeatedCharacters += [[i, j]]


		for square in squareSet:
			if len(set(square)) != uniqueCount:
				tmpSquareSet.remove(square)

		for square in tmpSquareSet:
			valid = True
			for repeatedCharacter in repeatedCharacters:
				a = repeatedCharacter[0]
				b = repeatedCharacter[1]
				if square[a] != square[b]:
					valid = False
					break
			if valid:
				squareAnagram = ''.join(anagram)
				for i in range(length):
					squareAnagram = squareAnagram.replace(word[i], square[i])
				if squareAnagram in squareSet:
					anagramSquareList.append(int(square))
					anagramSquareList.append(int(squareAnagram))
	if len(anagramSquareList) > 0:
		print(sorted(anagramSquareList)[-1])
		sys.exit(0)


