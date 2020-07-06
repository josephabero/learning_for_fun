class Employee:
	num_of_employees = 0
	raise_percent = 1.04

	def __init__(self, first_name, last_name, pay):
		# Instance Variables
		self.first_name = first_name
		self.last_name = last_name
		self.email = f"{first_name}.{last_name}@email.com"
		self.pay = pay

		Employee.num_of_employees += 1

	def get_full_name(self):
		return f"{self.first_name} {self.last_name}"

	def apply_raise(self):
		# Increases raise based on individual Employee (instance var)
		self.pay = int(self.pay * self.raise_percent)

		# Increases raise based on every Employee (class var)
		# self.pay = int(self.pay * Employee.raise_percent)

emp_1 = Employee("Joseph", "Abero", 50000)
emp_2 = Employee("Test", "User", 60000)

# Part 1
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.raise_percent)

print(Employee.raise_percent)
print(emp_1.raise_percent)
print(emp_2.raise_percent)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# Increase raise for ALL employees
Employee.raise_percent = 1.08
print(Employee.raise_percent)
print(emp_1.raise_percent)
print(emp_2.raise_percent)

# Only increase for Employee 1
emp_1.raise_percent = 1.06
print(Employee.raise_percent)
print(emp_1.raise_percent)
print(emp_2.raise_percent)

print(Employee.num_of_employees)