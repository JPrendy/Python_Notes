#Fizzbuzz test
fizz = "fizz"
buzz = "buzz"

for i in range(0,100):
    if i % 100 == 0:
        print(fizz + buzz + " " + str(i))
    if i % 3 == 0:
        print(fizz + " " + str(i))
    if i % 5 == 0:
        print(buzz + " " + str(i))

#Fibonacci Theorem
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    result = fib(n - 1) + fib(n - 2)
    return result

print(fib(13))

#the following will return factorial
def factorial(value):
    if value == 0:
        return 0
    if value == 1:
        return 1
    total = value * factorial(value - 1)
    return total

print(factorial(6))
