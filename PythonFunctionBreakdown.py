#Explanation on how to use functions in python
# remember to indent when in a function
def using_control_once():
    if True:
        return "Success #1"

#Instead of using function, that we would use in javascript, we use def, when creating a function
def using_control_again():
    if True:
        return "Success #2"

print (using_control_once())
print (using_control_again())

#==================================
#A bit more of a complicated python function

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False        # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False        # Make sure this returns False
      
print (black_knight())
print (french_soldier())

#=================================
#A function using if/else/else if

def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print (grade_converter(92))

# This should print a "C"
print (grade_converter(70))

# This should print an "F"
print (grade_converter(61))