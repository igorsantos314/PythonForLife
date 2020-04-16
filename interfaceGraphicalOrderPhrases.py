from tkinter import *
from OrderPhrases import phrase

class interfaceGraphPhrases:

    def __init__(self, P):
        self.P = P
        self.listPhrasesD = P.getlistPhrasesD()
        self.listPhrasesO = P.getlistPhrasesO()

        self.createWindowMain()

    #criar funcao para centralizar janela
    def centralizeWindow(self, x, y, w):

        #tamanho da tela
        lado = w.winfo_screenwidth()
        cima = w.winfo_screenheight()

        #alinhar
        top = int( (lado - (x/2)) / 2)
        bottom = int( (cima - (y/2))  / 2)

        #retorna o tamanho da tela proporcional
        return '{}x{}+{}+{}'.format(x, y, top, bottom)

    def createWindowMain(self):
        #window to menu
        self.window = Tk()
        
        #'200x200+500+50'
        self.window.geometry('300x200+500+50')
        self.window.title('Game to Learn English')

        #Button Start
        btStart = Button(text='Start Game', fg='white', bg='black', font='Arial 10 bold', width=15, height=4, command=self.startGame)
        btStart.pack()

        #button for choose lange
        btLanguage = Button(text='Choose Language', width=15, height=4, font='Arial 10 bold', fg='white', bg='black')
        btLanguage.pack()

        self.window.mainloop()

    def getWindow(self):
        return self.window

    def getPhrasesD(self):
        return self.listPhrasesD

    def getPhrasesO(self):
        return self.listPhrasesO

    def startGame(self):
        #destroy window
        self.getWindow().destroy()

        #lista ordenada
        listOrder = self.getPhrasesO()
        
        for pos, p in enumerate(self.getPhrasesD()):

            #janela temporaria
            windowTemp = Tk()
            windowTemp.title('Umount the Phrase')
            windowTemp['bg'] = 'black'

            #criar lista de labels para formar as palavras da frase
            WindowLabels = Tk()
            
            def createWindowLabels():
                WindowLabels.title('Keys Words')

                for word in p:  
                    lblTemp = Label(WindowLabels, text=word, width=12, height=4, font='Arial 12 bold', bg='black', fg='white')
                    lblTemp.pack(side=LEFT)


            #caixa de texto
            lblYourAnswer = Label(text='Your Phrase:', width=12, height=4, font='Arial 12 bold', fg='white', bg='black')
            lblYourAnswer.pack(side=LEFT)    

            #campo de resposta
            entryAnswer = Entry(font='Arial 20 bold', bg='black', fg='orange')
            entryAnswer.pack(side=LEFT)

            #funcao de comparação de reposta
            def compareAnswer():
                completeWord = ''
                phraseUser = entryAnswer.get().replace(' ','')

                for w in listOrder[pos]:
                    completeWord += w

                #todas as frases em minusculo para comparar
                completeWord = completeWord.lower().replace(' ','').replace('\n','')
                phraseUser = phraseUser.lower()
                
                #print(completeWord)
                #print(phraseUser)

                #comparar Respotas
                if completeWord == phraseUser:
                    print('Very Well')

                else:
                    print('Nothing Good')

                windowTemp.destroy()
                WindowLabels.destroy()

            #botao de confirmação
            btConfirmation = Button(text='OK', width=5, height=4, font='Arial 12 bold', bg='black', fg='white', command=compareAnswer)
            btConfirmation.pack(side=RIGHT)

            #montar janela
            createWindowLabels()

            #fecha janela apois fechar a outra
            windowTemp.mainloop()

        self.createWindowMain()

    def setlistPhrasesD(self):
        pass

P = phrase()
interfaceGraphPhrases(P)