response = 'Y'

answer = "Left"
if answer == "Left":
  print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    
#======================
#A more complicated version using if and elif

def plane_ride_cost_test(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

print("\n")
print (plane_ride_cost_test("Tampa"))


#==============================
#A more complicated of the above if statement using multiple functions
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)