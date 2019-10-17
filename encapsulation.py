#private and public methods and accessing them outside the class

class Hello:
    def __init__(self,name):
        self.a=10
        self._b=20
        self.__c=30
    def public_method(self):
        print(self.a)
        print(self.__c)
        print("public")
        self.__private_method()
    def __private_method(self):
        print("private")
hello=Hello("name")
print(hello.a)
print(hello._b)
hello.public_method()
#accessing private method outside the class: instance_name._classname__privatemethod()
hello._Hello__private_method()


#encapsulation, setter and getter 

class Car():
    def __init__(self,color,model):
        self.__color = color
        self.__model = model

    def move_forward(self):
        return self.__color,self.__model

    def set_model(self,value):
        self.__model = value

    def get_model(self):
        return self.__model

    def set_color(self,value):
        self.__color = value

    def get_color(self):
        return self.__color


first_car = Car("Brown","first")
second_car = Car ("Black","abc")

print (first_car.move_forward())
print (second_car.move_forward())

first_car.set_model("second")
print (first_car.get_model())

first_car.set_color("Blue")
print (first_car.get_color())
print (first_car.move_forward())



