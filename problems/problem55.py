#!/usr/bin/python
#Title: Lychrel numbers
import math

limit = 10000
maxDepthGlobal = 50
base = 10
palindromCounter = 0

digitStrings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def baseString(number, base):
	string = ""
	while number:
		string = digitStrings[number % base] + string
		number /= base
	return string

def isPalindrom(n, base):
	string = baseString(n, base)
	if string == string[::-1]:
		return True
	else:
		return False

def reverse(n, base):
	nReversed = 0
	tmp = n
	length = int(math.ceil(math.log(n + 1, base)))
	for i in range(length):
		nReversed += (tmp % base) * (base ** (length-i-1))
		tmp /= base
		#print nReversed
		#print tmp
	return nReversed

def createPalindrom_sub(n, base, maxDepth):
	#print n
	if maxDepth == 0:
		return False, False
	if not isPalindrom(n, base) or maxDepthGlobal == maxDepth:
		return createPalindrom_sub(n + reverse(n, base), base, maxDepth - 1)
	else:
		return baseString(n, base), maxDepth

def createPalindrom(n, base, maxDepth):
	palindrom, stepsLeft = createPalindrom_sub(n, base, maxDepth)
	if palindrom == False:
		print "no palindrom found for %s in %i steps" % (baseString(n,base), maxDepth)
		return False
	else:
		return True
	#else:
		#print "palindrom number for %s is %s in %i steps" % (baseString(n,base), palindrom, maxDepth-stepsLeft)

#createPalindrom(10, base, maxDepth)

for i in range(limit):
	if not createPalindrom(i, base, maxDepthGlobal):
		palindromCounter += 1
#for i in range(2, 20):
	#print "Base %i" %i
	#for j in range(limit):
		#createPalindrom(j, i, maxDepth)
print palindromCounter
