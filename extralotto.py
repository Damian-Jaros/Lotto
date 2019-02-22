
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import os
from totomodul import settings, drawnumbers, insertype, scores, cls

#def cls():
#	os.system('cls' if os.name=='nt' else 'clear')
def main(arg):
	#Clear screen
	cls()
	#Settings game
	nick, hownumb, maxnumb, howdraw = settings()

	#Drawn numbers
	numbers = drawnumbers(hownumb, maxnumb)

	#We download user types and veryfication how many numbers is correct
	for i in range(howdraw):
		type = insertype(hownumb,maxnumb)
		howhits = scores(set(numbers), type)

	print("Drawn numbers: %s" %(numbers))
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))


