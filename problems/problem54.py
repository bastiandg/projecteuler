#!/usr/bin/python
# -*- coding: utf-8 -*-
#Title: Poker hands

def handConvert(hand):
	newHand = []
	for card in hand:
		newHand.append([int(card[0], 16), int(card[1])])
	return newHand

def handEval(hand):
	if hand[0][0] == (hand[1][0] - 1) and\
		hand[1][0] == (hand[2][0] - 1) and\
		hand[2][0] == (hand[3][0] - 1) and\
		hand[3][0] == (hand[4][0] - 1):
			if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
				#print "STRAIGHT FLUSH!!! %r" % hand
				return 1000 + hand[4][0]
			else:
				#print "STRASSE %r %i" % (hand, hand[4][0])
				return 300 + hand[4][0]
	elif hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
		#print "FLUSH %r" % hand
		return 500 + hand[4][0]
	elif hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0] or\
		hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]:
		#print "4 OF A KIND %r %i" % (hand, hand[3][0])
		return 600 + hand[3][0]
	elif ( hand[0][0] == hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0] ) or\
			( hand[2][0] == hand[3][0] == hand[4][0] and hand[0][0] == hand[1][0] ):
		#print "FULL HOUSE %r %i" % (hand, hand[4][0])
		return 400 + hand[4][0]
	elif hand[0][0] == hand[1][0] == hand[2][0] or\
		hand[1][0] == hand[2][0] == hand[3][0] or\
		hand[2][0] == hand[3][0] == hand[4][0]:
		#print "3 OF A KIND %r %i" % (hand, hand[3][0])
		return 300 + hand[3][0]
	elif ( hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] ) or\
		( hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0] ) or\
		( hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0] ):
		#print "TWOPAIR %r %i" % (hand, hand[3][0])
		return 200 + hand[3][0]
	elif hand[0][0] == hand[1][0] or\
			hand[1][0] == hand[2][0]:
		#print "PAIR %r %i" % (hand, hand[1][0])
		return 100 + hand[1][0]
	elif hand[2][0] == hand[3][0] or\
			hand[3][0] == hand[4][0]:
		#print "PAIR %r %i" % (hand, hand[3][0])
		return 100 + hand[3][0]
	else:
		return hand[4][0]

p1wins = 0
f = open('poker54.txt', 'r')
hands = f.read().replace("C","1").replace("D","2").replace("S","3").replace("H","4").replace("A","E").replace("T","A").replace("J", "B").replace("Q", "C").replace("K", "D").split("\n")[:-1]
for hand in hands:
	hand = hand.split(" ")
	hand1 = sorted(hand[0:5])
	hand2 = sorted(hand[5:10])
	#print hand1
	#print hand2
	h1 = handEval(handConvert(hand1))
	h2 = handEval(handConvert(hand2))
	if h1 > h2:
		p1wins += 1
		print "P1 Wins %r - %r" % (hand1, hand2)
	elif h2 > h1:
		print "P2 Wins %r - %r" % (hand2, hand1)
	else:
		print "------------ DRAW %r - %r" % (hand1, hand2)

print "P1 Wins: %i" % p1wins

#print hands
