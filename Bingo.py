from random import sample

#list of numbers
numbers = []

def setList():
	for i in range(1, 76, 1):
		#add numbers from 1 to 100 to the list
		numbers.append(i)

def raffle():
	#return list drawed
	return sample(numbers, 75)

def start():
	#create list
	setList()

	#start bingo
	listRaffle = raffle()

	#print numbers of listRaffle and position
	for pos,i in enumerate(listRaffle):
		print("--> {}° Number: {} <--".format(pos+1, i))
		step = input('\n --> Press Enter to Continue .... <--')

#start raffle
start()