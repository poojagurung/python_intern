class Rectangle(object):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


a = Rectangle(2,3)
print (a.area())


        
#multiple inits

class Student():
    def __init__(self):
        pass

    def __init__(self,name):
        self.name = name 
        self.age = 20



a = Student("Ram")
print (a.name,a.age)
