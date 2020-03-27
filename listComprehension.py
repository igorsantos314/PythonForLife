#nothing list Comprehesion
for i in range(10):
    for j in range(10):
        print('line {}, col {}'.format(i,j))

#with list Comprehesion
listComp = [print('line {}, col {}'.format(i,j)) for j in range(10) for i in range(10)]