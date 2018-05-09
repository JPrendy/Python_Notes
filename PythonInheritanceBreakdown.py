class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print ("I'm a string that stands in for the contents of your shopping cart!")

#this is inheritanting from the class Customer
class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print ("I'm a string that stands in for your order history!")
  def displayCustomer(self):
    print("We are retrieving Customer ID from class we are inheriting {}".format(self.customer_id))

#create the instance here
monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
#this call will retrieve from a method in the
monty_python.displayCustomer()
monty_python.display_order_history()


#=========================================
#This examples looks at overriding the main class methods

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

#This calls the class Employee
test1 = Employee("James")
print(test1.calculate_wage(10))
#Override the method calutate_wage in the class "Employee"
test2 = PartTimeEmployee("James")
print(test2.calculate_wage(10))