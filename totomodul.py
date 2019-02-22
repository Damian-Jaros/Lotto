#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os

"""def cls():
	os.system('cls' if os.name=='nt' else 'clear')"""

def settings():
	#The function downloads name of user, how many numbers draw, upper number of draw numbers and numbers of type.
	#Settings is saving on file.
	nick = input("Enter your nick: ")
	usersett = nick + ".ini"
	player = read_sett(usersett)
	answ = None
	if player:
		print("Your settings: \nNumbers: %s\nMax: %s\nDrawings: %s" %(player[1], player[2], player[3]))
		answ = input("Change (Y/N)?")
	if not player or answ.lower() == "y":
		while True:
			try:
				hownumb = int(input("How many numbers you want to guess? \n"))
				maxnumb = int(input("The upper limit of random numbers: \n"))
				if hownumb > maxnumb:
					print("Error!")
					continue
				howdr = int(input("How many draws? \n"))
				break
			except ValueError:
				print("Incorrect data!")
				continue
		player = [nick, str(hownumb), str(maxnumb), str(howdr)]
		save_sett(usersett, player)

	return player[0:1] + [int(x) for x in player[1:4]]

def read_sett(usersett):
	if os.path.isfile(usersett):
		file = open(usersett, "r")
		line = file.readline()
		file.close()
		if line:
			return line.split(";")
	return False

def save_sett(usersett, player):
	file = open(usersett, "w")
	file.write(";".join(player))
	file.close()

def drawnumbers(hownumb, maxnumb):
	lotto = []
	i = 0
	while i < hownumb:
		number = random.randint(1,maxnumb)
		if lotto.count(number) == 0:
			lotto.append(number)
			i += 1
	return lotto

def insertype(hownumb, maxnumb):
	print("Choose %s numbers from %s numbers: " % (hownumb, maxnumb))
	choose = set()
	i = 0
	while i < hownumb:
		try:
			type = int(input("Please enter a number %s: " %(i+1)))
		except ValueError:
			print("Incorrect data!")
			continue
		if 0 < type <= maxnumb and type not in choose:
			choose.add(type)
		i = i + 1
	return choose

def scores(numbers, type):
	hits = set(numbers) & type
	if hits:
		print("The numbers of hits is %s" %len(hits))
		hits = ", ".join(map(str, hits))
		print("Hit numbers: %s" % hits)
	else:
		print("You don't hit anything, please try again!")
	print ("\n"+"x"*40 +"\n")
	return len(hits)

def cls():
	import os
	os.system('cls' if os.name=='nt' else 'clear')
