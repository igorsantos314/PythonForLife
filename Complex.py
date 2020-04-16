from random import sample

class phrase:
    def __init__(self):
        self.street = '/home/igor/Área de trabalho/PythonForLife/'
        self.listPhrases = []

        self.getPhrasesArq()
        self.orderList()

    def getStreet(self):
        return self.street

    def setListPhrases(self, newPhrase):
        self.listPhrases.append(newPhrase)

    def getListPhrases(self):
        return self.listPhrases

    def changeListPhrase(self, newList):
        self.listPhrases = newList
        
    def orderList(self):
        numberElements = len(self.getListPhrases())
        self.changeListPhrase( sample(self.getListPhrases(), numberElements) )
    
    def orderWords(self, Phrases):
        numberWords = len(Phrases)

        return sample(Phrases, numberWords)

    def getWords(self, Phrase):

        posInit = 0
        listWords = []

        for pos,i in enumerate(Phrase):
            word = ''

            if i == ' ':
                
                for i in range(posInit, pos):
                    word += Phrase[i]
                    
                listWords.append(word)
                posInit = pos+1

        return self.orderWords(listWords)
        
    def getPhrasesArq(self):
        ArqPhrases = open('{}Phrases.txt'.format(self.getStreet()), 'r', encoding='latin-1')
        
        for i in ArqPhrases:
            if i == '' or i == '\n':
                pass

            else:
                i = i.replace('\n', ' ')
                element = self.getWords(i)

                self.setListPhrases(element)

        ArqPhrases.close()

P = phrase()
print(P.getListPhrases())