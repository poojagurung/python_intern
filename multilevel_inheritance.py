#example 1

class vehicle():
    def __init__(self,type,brand):
        self.type = type
        self.brand = brand

    def display(self):
        print (f"It is a {self.type} and it is of brand {self.brand}")

class bike(vehicle):
    def bike_disp(self):
        print (f"The bike is of brand {self.brand}")

class electrical_bike(bike):
    def __init__(self,type,brand,electrical):
        super().__init__(type,brand)
        self.electrical = electrical

    def print_electrical(self):
        if self.electrical == True:
            print ("It is an electrical bike.")
        else:
            print ("It is not an electrical bike.")

v1 = electrical_bike("two-wheeler","Honda",True)
v1.display()
v1.bike_disp()
v1.print_electrical()


#example 2

class Animals():
    def  __init__(self,name,type):
        self.name = name
        self.type = type
    
class Land_animals(Animals):
    def __init__(self,name,type,habitat):
        super().__init__(name,type)
        self.habitat = habitat

class Mammals(Land_animals):
    def __init__(self,name,type,habitat,lifespan):
        super().__init__(name,type,habitat)
        self.lifespan = lifespan
    
    def display(self):
        print (f"The name of the animal is {self.name}. It is a {self.type} which lives in the {self.habitat}.It has a life span of {self.lifespan} years.")
    
a1 = Mammals("Camel","Land animal","desert","10")
a1.display()


#example 3 (executing example 2 by asking for input)

class Animals():
    def get_animal(self):
        self.name = input ("Enter the name of animal: ")
        self.type = input ("What type of animal is it? ")
    
class Land_animals(Animals):
    def get_habitat(self):
        self.habitat = input ("Where does it live ?")

class Mammals(Land_animals):
    def get_lifespan(self):
        self.lifespan = input ("Enter the lifespan of animal: ")
    
    def display(self):
        print (f"The name of the animal is {self.name}. It is a {self.type} which lives in the {self.habitat}.It has a life span of {self.lifespan} years.")
    
a1 = Mammals()
a1.get_animal()
a1.get_habitat()
a1.get_lifespan()

a1.display()