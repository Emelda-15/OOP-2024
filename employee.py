class Employee:
    # Class variable
    retirement_age = 65

    def __init__(self, name, age):
        self.name = name  
        self.age = age

    def years_until_retirement(self):
        return Employee.retirement_age - self.age

# Create employees
emp1 = Employee("Sheba", 25)
emp2 = Employee("Gavin", 45)

print(emp1.years_until_retirement())
print(emp2.years_until_retirement())  
