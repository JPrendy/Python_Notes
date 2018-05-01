#Examples that breakdown for loops in python

#In this example we are going over how for loops are used in Python
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for val in names:
  print(val)

#================================================
#this example of a for loop goes through a dictionary
print("\n")
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for val in webster:
  print("This will print the keys " + val)
  print("This will print the value " + webster[val])
  

#================================
#An example of a for loop breakdown using if condition
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in a:
  if num % 2==0:
    print (num)


#===============================
#Another example that looks at a Python breakdown
# Write your function below!
def fizz_count(x):
  count = 0
  
  for item in x:
    if item == "fizz":
      count += 1
    
  return count

print(fizz_count(["fizz", "cat", "fizz"]))

#==========================================
#An example that goes over a while loop
count = 0

while count < 10: # Add a colon
  print(count)
  count +=1

#==========================================
#Classic for loop breakdown
#instead of normally of how we do for(i=0;i<3;i++), we do the
#following like down below, it will print out 0,1,2
for x in range(0, 3):
    print ("We're on time %d" % (x))



#Doing the for loop like so in Python will print every number from 0 to 7
for value in range(7):
    print (value)
