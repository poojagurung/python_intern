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


#simple inheritance example

class Polygon():
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth

  def disp(self):
    print (f"The length is {self.length} and breadth is {self.breadth}")

class Rectangle(Polygon):
  def __init__(self,length,breadth):
    super().__init__(length,breadth)

  def area(self):
    area = 0.5 * self.length* self.breadth
    print (f"Area of rectangle is: {area}" )

p1 = Rectangle(5,3)
p1.disp()
p1.area()


#example 2

class Student():
   def __init__(self,student_name):
       self.student_name = student_name
   def get_name(self):
       print (f"Student name is {self.student_name}")
class Teacher(Student):
   def __init__(self,student_name,teacher_name,teaching_subjects,salary):
       super().__init__(student_name)
       self.teacher_name = teacher_name
       self.teaching_subjects =  teaching_subjects
       self.salary = salary
   def print_teacher(self):
       print (f"{self.student_name} is taught by {self.teacher_name}")

teacher1= Teacher("Hari","Binita Sharma","science",20000)
teacher1.get_name()
teacher1.print_teacher()
