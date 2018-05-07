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

#============================================
#More complex exercise questions
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for val in students:
  print(val["name"])
  print(val["homework"])
  print(val["quizzes"])
  print(val["tests"])

#==================================================

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  
  total = homework *.1 + quizzes * .3 + tests * .6
  return total

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  
  
  
print(get_letter_grade(get_average(lloyd)))



#====================================================
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [alice, lloyd, tyler]
print(get_class_average(students))
# Add your function below!
def average2(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average2(student):
  homework = average2(student["homework"])
  quizzes = average2(student["quizzes"])
  tests = average2(student["tests"])
  
  total = homework *.1 + quizzes * .3 + tests * .6
  return total

def get_letter_grade2(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  
  
  
print(get_letter_grade2(get_average2(lloyd)))

def get_class_average(class_list):
  results=[]
  for student in class_list:
    result = get_average(student)
    results.append(result)
    
  return average(results) 