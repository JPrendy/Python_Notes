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