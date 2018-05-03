#The following will return the fibonacci numbers
def fib(n):
   if n ==0:
       return 1 
   if n == 1:
        return 0
   result = fib(n - 1) + fib(n -2)
   return result

print(fib(13))

#the following will return factorial
def fac(value):
    if value == 0:
        return 0
    if value == 1:
        return 1
    total = value * fac(value -1)
    return total

print(fac(4))
print(fac(5))
print(fac(6))