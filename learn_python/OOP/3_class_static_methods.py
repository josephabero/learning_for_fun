import datetime

class Employee:
	num_of_employees = 0
	raise_amount = 1.04

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
		self.pay = int(self.pay * self.raise_amount)

		# Increases raise based on every Employee (class var)
		# self.pay = int(self.pay * Employee.raise_amount)

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount


	# Can use class methods as an alternative constructor
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split("-")
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		return day.weekday() != 5 and day.weekday() != 6

emp_1 = Employee("Joseph", "Abero", 50000)
emp_2 = Employee("Test", "User", 60000)


# Part 1
# Call class method to set each employee's raise amount
Employee.set_raise_amount(1.06)
# Can still call class method from instance, but whyyy
emp_1.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Part 2: Using class methods as Alternative Constructors

emp_str_1 = "John-Doe-70000"

# first, last, pay = emp_str_1.split("-")
# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)


# Part 3: Static Methods
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))