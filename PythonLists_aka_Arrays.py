#In python arrays are called lists, however they operate closely how we used them in javascript

#A simple example of pythons lists
numbers = [5, 6, 7, 8]
print (numbers[1] + numbers[3])

#An example of replacing a value in a list
numbers = [5, 6, 7, 8]
print(numbers[0])
print("\n")
numbers[0]= 15
print(numbers[0])

#an example of adding a value to the end of a list
numbers = [5, 6, 7, 8]
numbers.append(11)
#print the entire list
print(numbers)


#an example of a list using slicing
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]
print(first)
# Third and fourth items (index two and three)
middle = suitcase[2:4]
print(middle)
# The last two items (index four and five)
last = suitcase[4:6]  
print(last)

#==================================
#The following will look an array item index

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
print (duck_index)

#the following will add to the array depending where you want to add it
animals.insert(2, "cobra")

print (animals) # Observe what prints after the insert operation

#=========================================
#A for loop using arrays

my_list = [1,9,3,8,5,7]

#So, number will be assigned my_list[0], my_list[1], my_list[2] and you can do with number whatever you want
for number in my_list:
  print (2 * number)
  # Your code here
  
#========================================
#A rundown of sort and a more complex problem using lists
start_list = [5, 3, 1, 2, 4]

square_list = []
for x in start_list:
  square_list.append(x ** 2)

#Outside of the for loop
square_list.sort()

print(square_list)

#=========================================
#An example that looks at deleting items from a list
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove('dagger')
print(backpack)