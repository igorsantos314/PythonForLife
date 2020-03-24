import math
from tkinter import *
import _thread as th
from time import sleep

janela  = Tk()
janela.geometry('500x500')

listaVals = []
listaPosition = []

def lim():
    x = 0 

    for i in range(20):
        #res = math.sqrt(x ** 2 + x + 1) + x
        res = 2*x + 1
        x -= 0.1
        
        if len(listaVals) == 0:
            pass

        elif listaVals[-1] > res:
            listaPosition.append('Up')

        elif listaVals[-1] < res:
            listaPosition.append('Down')

        elif listaVals[-1] == res:
            listaPosition.append('Const')

        listaVals.append(res)

def behaviorFunction():

    posX = 10
    posY = 250

    listPoints = []
    
    for i in listaPosition:
        
        lblPoint = Label(text='*', fg='red')
        listPoints.append(lblPoint)

    for pos, p in enumerate(listaPosition):
        if p == 'Up':
            posX += 2
            posY -= 2

        elif p == 'Down':
            posX += 2
            posY += 2

        elif p == 'Const':
            posX += 2
        
        listPoints[pos].place(x=posX, y=posY)
        
        sleep(0.5)
    
lim()
print(listaPosition)
th.start_new_thread(behaviorFunction, ())

janela.mainloop()
