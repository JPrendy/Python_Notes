#In python enumerate is provided
#enumerate works by supplying a corresponding
#index to each element in the list that you pass it.

#For example, in the work below
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
#this works by setting index to 0,1,2,3 and then item is then set to "pizza, pasta, salad, nachos"
#the keyprases can be anything not just index and item, however you do need "enumerate"
for index, item in enumerate(choices):
  print(index, item)

#we will get the following
# Your choices are:
# 0 pizza
# 1 pasta
# 2 salad
# 3 nachos