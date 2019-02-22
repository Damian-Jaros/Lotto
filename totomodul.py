
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

"""def cls():
	os.system('cls' if os.name=='nt' else 'clear')"""

def settings():
	while True:
		try:
			hownumb = int(input("How many numbers you want to guess? \n"))
			maxnumb = int(input("The upper limit of random numbers: \n"))
			if hownumb > maxnumb:
				print("Error!")
				continue
			howdr = int(input("How many draws? \n"))
			return (hownumb, maxnumb, howdr)
		except ValueError:
			print("Incorrect data!")
			continue


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
