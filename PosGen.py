#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:
import random

def yCoord(x):
	return random.randint(0, x)

def xCoord():
	list = ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
	return random.choice(list)

def coinFlip():
	coins = [True, False]
	return random.choice(coins)

def makePlayers(x):
	playerCoords = []
	for i in range(x):
		playerCoords.append((str(xCoord()) + ' - ' + str(yCoord(15))))
	players = list(set(playerCoords))
	if len(playerCoords) != len(players):
		makePlayers(x)
	else:
		return players


coin = coinFlip()
count = 0
count = int(input("how many players? ") or '0')

positions = makePlayers(count)
for x in positions:
	print(x)
 
print('Heart at', xCoord(), '-', yCoord(15))

if coin:
	print('AP positioned at', end=' ')
	print(xCoord(), '-', yCoord(15))
else: 
	print('No AP today')