prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

#here is value is basically banana, apple, etc and since both dictionaries have both objects called the same
for val in prices:
  print (val)
  print ("price: " + str(prices[val]))
  print ("stock: " + str(stock[val]))

#this part looks at combining prices and stock dictionaries
total = 0

for val in prices:
  print(prices[val] * stock[val])
  total += prices[val] * stock[val]
  
  
print(total)

#=============================
#Another version of the SuperMarket Exercise

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total = total + prices[item]
      stock[item] -=1
  return total


print(compute_bill(shopping_list))
