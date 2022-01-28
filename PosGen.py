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

print('Heart at', xCoord(), '-', yCoord(15))
coin = coinFlip()


if coin:
	print('AP positioned at')
	print(coin, xCoord(), '-', yCoord(15))
else: 
	print('No AP today')