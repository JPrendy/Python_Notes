#The following goes over the basics of Python3
# For example, str(), abs(), min(), max(), upper(), lower(), input, type and len()

testOne = max(1,3,5) #returns max 5
testTwo = min(-1,4, 7) #return min -1
abs(-10) #returns 10 makes it positive

#to get a type of a value use type, for example
print (type("hello"))


testVar = "Hello, this is amazing, Wowser"
age = 13
print(testVar)
#len returns it as a number, so we then make the int into a string
print(len(testVar))
print("the length of testVar is " + str(len(testVar)))

print("I am " +str(age))
print (testVar.lower())
print (testVar.upper())
"""
to make items a string, integer and float
use int(), float() and str() to convert the variabless

"""

string_1 = "Camelot"
string_2 = "place"
#similar to how it is done in c
print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

#input looks for whatever value you add in the console.
name = input("What is your name? ")
print ("nice name " + name)

#this retrieves the current time
from datetime import datetime
now = datetime.now()
print (now)

