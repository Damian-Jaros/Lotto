
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

number = random.randint(1, 3)
print ("Select number: ", number)

for i in range(3):
	print ("Attempt: " ,i+1)
	print ("Select the drawn number")
	choise = input ()
	#print ("You have chosen a number:", choise)

	if int(choise) == number:
		print("You won!")
		break
	elif i==2:
		print("We selected number: ",number)

	else:
		print("You lose :(")


#print ("Drawn number:",number)
