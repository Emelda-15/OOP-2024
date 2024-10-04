class Car:
    def __init__(self, make, model, year):
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
    
    def display_info(self):
        return f"Car: {self.year} {self.make} {self.model}"

# Creating an object
my_car = Car("Toyota", "Camry", 2021)
print(my_car.display_info())
