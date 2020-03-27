import matplotlib.pyplot

#return value of funcition
def getValue(x):
    #8x² – 4x  + 1
    return 8 * x**2 - 4*x + 1

#values of -3 at 4
valoresX = [i for i in range(-3, 4)]

ValorFx = [getValue(x) for x in valoresX]

#send values for library
matplotlib.pyplot.plot(valoresX, ValorFx)

#create graph
matplotlib.pyplot.show()






