class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary

#private function
    def _printsalary(self):
        return self.__salary


e = Employee("Ram",25000)

print (e.name)
#accessing private function
print (e._printsalary())
#accessing private variable 
print (e._Employee__salary)
