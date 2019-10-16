class Triangle(object):
  number_of_sides = 3
  def __init__(self,angle1,angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    sum = self.angle1 + self.angle2 + self.angle3
    if sum == 180:
      return True
    else:
      return False
    
a = Triangle(40,60,80)
print (Triangle.check_angles(a))

my_triangle = Triangle(40,60,80)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = angle
        self.angle2 = angle
        self.angle3 = angle



#inheriting from parent class using super

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
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print (milton.full_time_wage(10))
