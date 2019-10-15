#Some basic functions

def addition(a,b):
    result = a + b
    return result

print (addition(2,5))


def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total

print (factorial(6))


#creating classes and functions using oop

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_biggest_number(*age):
        result=0
        for item in age:
            if item > result:
                result= item
        return result
            

Sam = Student("Sam",18)
Peter = Student("Peter",20)
Karen = Student("Karen",22)
Mike = Student("Michael",21)

oldest= Student.get_biggest_number(Sam.age,Peter.age,Karen.age,Mike.age)
print (f"The oldest student is {oldest} years old.")



class Animal(object):
    is_alive = True
    def __init__(self, name, age,is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)


class ShoppingCart(object):
  
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print (product + " added.")
    else:
      print (product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print (product + " removed.")
    else:
      print (product + " is not in the cart.")

my_cart = ShoppingCart("Max")
my_cart.add_item("Apples",150)
my_cart.add_item("Juice",100)
my_cart.remove_item("Juice")
