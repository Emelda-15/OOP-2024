class Vehicle:
    def __init__(self, color):
        self.color = color

    # method to get color
    def getColor(self):
        return self.color

    # method to represent the object as a string
    def __str__(self):
        return f"The vehicle is {self.color}."

# Creating an instance of Vehicle
vehicle1 = Vehicle("green")

# Printing the object to see the output of __str__
print(vehicle1)

# Car class extending Vehicle
class Car(Vehicle):
    def __init__(self, color, winter_tires=False):
        super().__init__(color)  # Calls the constructor of Vehicle
        self.winter_tires = winter_tires

    def __str__(self):
        vehicle_str = super().__str__()  # Calls the __str__ method of Vehicle
        return f"{vehicle_str}\nHas winter tires: {self.winter_tires}."
    
    # Truck class extending Vehicle
class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)  # Calls the constructor of Vehicle
        self.has_trailer = has_trailer

    def __str__(self):
        vehicle_str = super().__str__()  # Calls the __str__ method of Vehicle
        return f"{vehicle_str}\nHas trailer: {self.has_trailer}."
    
        # Garage class that can park a Vehicle (either a Car or Truck)
class Garage:
    def __init__(self):
        self.parked_vehicle = None  # Initially, no vehicle is parked

    def setVehicle(self, parked):
        self.parked_vehicle = parked  # Park a vehicle in the garage

    def __str__(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle}"
        else:
            return "The garage is empty."
        