#example 1

class Employee(object):
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super().calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print (milton.calculate_wage(10))
print (milton.full_time_wage(10))


#example 2

class A():
    def display(self):
        print ("This is inside class A")

    def printing(self):
        print ("This is another method inside class A")

class B(A):
    def display(self):
        print ("This is inside class B")

a1 = B()
a1.display()
a1.printing()