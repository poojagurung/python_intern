class Dog():
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

class Cat():
    def __init__(self,name):
        self.name = name

class Animal(Dog,Cat):
    def __init__(self,breed,color,name):
        Dog.__init__(self,breed,color)
        Cat.__init__(self,name)

    def display(self):
        print (f"The name of animal is {self.name}. It is of {self.color} and breed is {self.breed}")

an = Animal("german shepard", "brown", "jack")
print (an.name)
an.display()
