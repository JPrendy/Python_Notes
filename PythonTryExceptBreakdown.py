#this example of while loop will go on forever until a number is entered
while True:
    try:
        number = int(input("Please Enter a number: "))
        #when a number is entered it will call brak, which call anything after the while loop
        break
    except:
        print("You didn't enter a numer")

#this is called after the break keyword is called
print("We are past the while loop.")