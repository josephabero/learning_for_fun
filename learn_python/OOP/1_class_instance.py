# Python Object-Oriented Programming

class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}.{last_name}@email.com"
        self.pay = pay

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


emp_1 = Employee("Joseph", "Abero", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1.email)
# print(emp_2.email)

# Function call with class instances
print(emp_1.get_full_name())
print(emp_2.get_full_name())

# Class call by passing in class instance
# (Same thing)
print(Employee.get_full_name(emp_1))