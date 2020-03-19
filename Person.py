class Person:

    name = ''
    age = 0
    height = 0
    weight = 0

    #constructor
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    #gets
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    #sets
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setHeight(self, height):
        self.height = height

    def setWeight(self, weight):
        self.weight = weight

    #data of Person
    def printData(self):
        print(' --> Name: ',self.name)
        print(' --> Age: ',self.age)
        print(' --> Height: ',self.height)
        print(' --> Weight: ',self.weight)

#create persons Mary and John
mary = Person('Mary', 19, 1.75, 75)
john = Person('John', 25, 1.80, 95)

#change data of mary
mary.setWeight(90)
mary.setWeight(20)

#change data of john
john.setHeight(1.85)
john.setAge(26)

mary.printData()
john.printData()








