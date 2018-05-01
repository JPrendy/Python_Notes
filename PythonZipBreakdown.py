#If you want to go over two lists at a time, there is the built
#in zip function in Python

#zip will stop at the end of the shortest list, aka if there are 5 items in list one
#and 10 items in list two, it will end after the 5th item 

#zip can handle three or more lists as well

#An example of using the zip function 
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
list_c = [3, 5, 7, 9, 11, 21, 33, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print(a,b)

#this will return the following
#3 2
#9 4
#17 8
#15 10
#19 30
print("\n")

#this version will be comparing them
for a, b in zip(list_a, list_b):
  if a > b:
    print(a)
  else:
    print(b)
  
print("\n")

#this version will be comparing three lists
for a, b, c in zip(list_a, list_b, list_c):
  print(a,b,c)
  
