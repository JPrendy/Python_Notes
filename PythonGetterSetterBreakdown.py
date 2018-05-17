# The purpose of this is that we want our field to be private so that they can't
# be accessed without going through the getter/setter method.

# But, if you provide a getter/setter, you provide them indirect access while taking full control. The only way to set a value is through setter, and you get a value through a getter, so now you have exactly one entry and one exit point for your field, as getter/setters are methods,
#  which allows blocks of code, so you can do validation checks on them! 

class Square:
    def __init__(self,height):
        self.height = height

# For the following, you will need the tags @property and @height.setter,
# to make getter and setter to work

#the names should be the same as the one applied in the __init__

    #this is the getter which returns the value
    @property
    def height(self):
        #returns the following private field
        return self.__height
    @height.setter
    def height(self, value):
        if value == 0:
            print("woops, please do not enter 0")
        else:
            self.__height=value


def main():
    #when working with getter and setter it is not needed to use () tags to call the method
    newSquare = Square("")
    height = 0
    newSquare.height = height
    print(newSquare.height)

main()
