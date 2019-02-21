

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random, os

def cls():
	os.system('cls' if os.name=='nt' else 'clear')
cls()
try:
	hownumb = int(input("How many numbers you want to guess? \n"))
	maxnumb = int(input("The upper limit of random numbers: \n"))
	if  maxnumb<hownumb:
		print("Error!")
		exit()
except ValueError:
	print("Błędne dane!")
	exit()
#print ("Choose" , hownumb, "numbers from" ,maxnumb, "numbers:")
#print("Choose %s numbers from %s numbers: " % (hownumb, maxnumb))
lotto = []
#for i in range(hownumb):
i = 0
while i < hownumb:
	number = random.randint(1,maxnumb)
	if lotto.count(number) == 0:
		lotto.append(number)
		i += 1
#print ("Drawn numbers: %s" % (lotto))
for i in range(3):
	print("Choose %s numbers from %s numbers: " % (hownumb, maxnumb))
	choose = set()
	i=0
	while i<hownumb:
		try:
			type =int(input("Please enter a number %s: " %(i+1)))
		except ValueError:
			print("Błędne dane!")
			continue
		if 0 < type <= maxnumb and type not in choose:
			choose.add(type)
			i+=1
	#print(choose)
	hits = set(lotto) & choose
	#print (hits)
	if hits:
		print("The numbers of hits is %s" %len(hits))
		print("Hit numbers: ", hits)
	else:
		print("You don't hit anything, please try again!")
	print ("\n"+"x"*40 +"\n")
print("Drawn numbers: %s" %(lotto))

