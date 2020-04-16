from tkinter import *
from random import randint, sample, choice

class bingo:

    def __init__(self):
        
        #list of Numbers
        self.listNumbers = sample([i for i in range(1, 76)], 75)

        #matriz of Labels
        self.listLabels = []

        self.window = Tk()
        self.window.geometry("600x600")

        #create list of Labels
        self.createListLabels()

        #Raffle
        btRaffle = Button(text='Raffle', command=self.Raffle)
        btRaffle.pack()

        self.window.mainloop()

    def createListLabels(self):
        posx = 50
        posy = 50

        #lines
        for i in range(8):
            listBt = []

            #columns
            for j in range(10):
                
                #create last line
                if i == 7 and j > 5:
                    pass
                
                else:
                    bt = Label(text='', width=4, height=2, bg='black', fg='white', font="Arial 12 bold")
                    bt.place(x=posx, y=posy)
                    listBt.append(bt)
                    posx += 50

            #add list into Matriz
            self.listLabels.append(listBt)
            
            #positionss
            posy += 50
            posx = 50
            
        self.listLabels[0][0]["text"] = 'B'

    def Raffle(self):
        
        if len(self.listNumbers) > 0:
            #get first number and remove
            n = self.listNumbers[0]
            print(n)
            self.listNumbers.remove(n)

            #get digits
            nString = str(n)

            #send numbers
            if len(nString) == 1:
                self.showValue('0',nString)

            else:
                self.showValue(nString[0], nString[1])

    def showValue(self, n1, n2):
        #with digits get position x and y
        x = int(n1)
        y = int(n2)

        #set value raffled
        self.listLabels[x][y]['text'] = "{}{}".format(n1, n2)

bingo()