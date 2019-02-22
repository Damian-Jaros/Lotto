#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from totomodul import settings, drawnumbers, insertype

def main(arg):
	#Clear screen
#	cls()
	#Settings game
	hownumb, maxnumb, howdraw = settings()

	#Drawn numbers
	numbers = drawnumbers(hownumb, maxnumb)

	#We download user types and veryfication how many numbers is correct
	for i in range(howdraw):
		type = insertype(hownumb,maxnumb)
		hits = set(numbers) & type
		if hits:
	                print("The numbers of hits is %s" %len(hits))
        	        print("Hit numbers: ", hits)
		else:
        	        print("You don't hit anything, please try again!")

		print ("\n"+"x"*40 +"\n")
	print("Drawn numbers: %s" %(numbers))
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))


