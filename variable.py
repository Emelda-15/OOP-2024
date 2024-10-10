class Car:
    # Class variable
    wheels = 4

    def __init__(self, model):
        self.model = model  # Instance variable

    @classmethod
    def change_wheels(cls, num_wheels):
        cls.wheels = num_wheels  

# Call class method
Car.change_wheels(6)

print(Car.wheels)  
