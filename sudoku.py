from random import *

def getNumbers():
	listValues = [i for i in range(0,9)]
	listPositions = [i for i in range(0,3)]

	return [sample(listValues, 3), sample(listPositions, 3)]

def setMatriz():

	matriz = [[0,0,0],[0,0,0],[0,0,0]]
	numberPositions = getNumbers()

	for pos,i in enumerate(numberPositions[1]):
		matriz[pos][i] = numberPositions[0][pos]

	#exibe e inicia o jogo
	printMatriz(matriz)
	start(matriz)

def start(matriz):

	while True:
		print("\n 		============> EX: line 2 and column 1: 21 ============>\n")
		pos = input("		-> Digite a Posicao: ")

		v = int(input("			-> Valor:"))

		pX = int(pos[0]) - 1
		pY = int(pos[1]) - 1

		if setValue(pX, pY, v, matriz):
			matriz[pX][pY] = v
		else:
			print("			--> Incorrect Value ! <--")

		printMatriz(matriz)
		winer(matriz)

def winer(matriz):
	for i in matriz:
		if sum([j for j in i]) == 10:
			print("\n\n 		## --> Line {} OK! <-- ##\n\n")

def setValue(pX, pY, v, matriz):

	status = False

	if  pX > 2 or pX < 0 or pY > 2 or pY < 0:
		return status

	elif matriz[pX][pY] != 0 or v > 9 or v < 0:
		return status

	return True 

def printMatriz(matriz):

	for i in matriz:
		print(*i)


setMatriz()