def getGrades():

    listGrades = []

    #get 4 grades and return average
    for i in range(4):
        grade = float(input('{}° grade: '.format(i+1)))

        #add in list fo grades
        listGrades.append(grade)

    #return average
    return sum(listGrades) / 4

def main():

    average = getGrades()

    print(' --> Your Average: ', average)
    
    #if average equals ten
    if average == 10:
        print('>> Very Good °o° <<')

    #if average greater than six
    elif average >= 6:
        print('>> Appoved Student :) <<')

    #if average smaller than six
    elif average < 6:
        print(' >> Reproved Student :( <<')

#call function
main()