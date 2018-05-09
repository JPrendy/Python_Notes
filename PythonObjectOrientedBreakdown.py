#this is a quick example of how classes work in python, instead of calling 'dog' in the constructor we use __init__
class Dog:
#You can think of __init__() as the function that "boots up" each object the class creates.
    def __init__(self, name="Default", height=0, weight=0 ):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("Wow {} is really fast".format(self.name))
    def describe(self):
        print("Wow {} is {} and weighs {}".format(self.name, self.height, self.weight))

#this is the default function that everything runs first
def main():
    Rex = Dog("Rex")
    Rex.run()
    Rex.describe()
#this will print "Wow Rex is 0 and weighs 0" because they are the default for height and weight and we didn't mention his specific
# attributes when creating his object    
    Sally = Dog("Sally", 120, 140)
    Sally.describe()
#While Sally will work and print out "Wow Sally is 120 and weighs 140"

main()

#===============================================
#Another quick example of how object oriented works in Python

class Animal(object):
  
  def __init__(self, name):
    self.name = name
    
zebra = Animal("Jeffrey")
print(zebra.name)  

#===============================================
#Another quick example of Object Oriented


class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

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

my_cart = ShoppingCart("James")
my_cart.add_item("eggs", 2)


#====================================
#Another quick example of Object Oriented in Python
class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


#======================================
#Another quick example
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg
 

my_car = Car("DeLorean", "silver", 88)
print(my_car.condition)
print(my_car.model)
print(my_car.color)
print(my_car.mpg)