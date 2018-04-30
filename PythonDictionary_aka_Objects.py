# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin']) # Prints Puffin's room number
print (residents['Sloth'])

print (residents['Burmese Python'])

# Your code here!

#==========================================
# A more complex look of dictionaries and what you can add to dictionaries

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['lamb'] = 4
menu['steak'] = 5
menu['roast potato'] = 7


print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)