class Vehicle: 
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        
    def start(self):
        print(f"The {self.vehicle_type} is starting")
        
class Car(Vehicle):
    def __init__(self, vehicle_type, number_of_doors):
        super().__init__(vehicle_type)
        self.number_of_doors = number_of_doors
        
class ElectricCar(Car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity):
        super().__init__(vehicle_type, number_of_doors) 
        self.battery_capacity = battery_capacity      
        
    def show_details(self): 
        print(f"Vehicle type: {self.vehicle_type} Doors:{self.number_of_doors} Battery capacity:{self.battery_capacity}kwh")
        
electric_car1 = ElectricCar("Electric car", 6, 87)
electric_car1.start()
electric_car1.show_details                                 
        