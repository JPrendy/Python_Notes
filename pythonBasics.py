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

