#convert miles into kilometres exercise
def convert(miles):
    kilometres = miles * 1.60934
    return kilometres

value = input("Enter miles ")
value = int(value)
print(convert(value))

print("Another way of wrinting in python {}".format(value))

#if statement looking at age the user inputs
#eval converts string to int
age = eval(input("Enter your Age: "))
if age == 5:
    print("Go to KinderGarden")
elif age >= 6 and age <= 17:
    grade = age - 5
    print("Go to grade {}".format(grade))
elif age >=  17:
    print("Go to college")
else:
    print("You are too young to go to school")

#An exercise printing out the odd numbers of an exercise
for i in range(0, 21):
    if i % 2 == 1:
        print("i = ",i)

#Get expected interest rates plus interest rates
value1 =  eval(input("Enter amount :"))
value2 = eval(input("Enter interest rate :"))
total = 0
for i in range(10):
    total += value1 + (value1 * value2) 
  
print("The final total is ", total)