class Smartphone:
    def __init__(self, brand, model, storage_capacity, battery_life):
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity
        self.battery_life = battery_life
    
    def make_call(self, contact):
        print(f"Calling {contact} from {self.model}...")
    
    def check_battery(self):
        print(f"{self.model} has {self.battery_life}% battery remaining.")

# Example of creating an object
phone1 = Smartphone("Apple", "iPhone 13", "128GB", 85)
phone1.make_call("David")
phone1.check_battery()
