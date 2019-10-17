class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary

#private function
    def __printsalary(self):
        return self.__salary


e = Employee("Ram",25000)

print (e.name)
#accessing private variable outside the ckass
print (e._Employee__salary)
