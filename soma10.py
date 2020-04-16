from random import* 
listValues = [i for i in range(10)]

def valTeen():
	matriz = []

	while True:
		l = sample(listValues, 3)
		s = sum(l)

		if len(matriz) == 3:
			break;

		if s == 10:
			matriz.append(l)
			print(l)

			for i in l:
				listValues.remove(i)

	print(matriz)

valTeen()
