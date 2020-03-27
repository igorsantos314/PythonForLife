#change characters of string
def changeString(phrase, a, c):

    return phrase.replace(a, c)

#get strings
yourPhrase = input('Phrase: ')

#get character for Replace
charactereReplace = input('Character for Replace: ')

#get new charater
newCharacter = input('New Character: ')

#storage the new string
newString = changeString(yourPhrase, charactereReplace, newCharacter)

print('\n>> New Phrase <<\n', newString)





