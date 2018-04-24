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


#==================================
# An example where a function calls another function

def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

print (one_good_turn(4))
print (deserves_another(5))


#=================================
# Another example using functions
def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

#remember "\n" prints the content to a newline
print("\n")  
print (cube(4))
print (by_three(9))
print (by_three(10))

#============================
#A function that checks if it is type int or float
def distance_from_zero(name):
  if type(name) == int or  type(name) == float:
    return abs(name)
  else:
    return "Nope"
  
print(distance_from_zero("ok"))