class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.open_status = False
    
    def open_restaurant(self):
        self.open_status = True
        print(f"{self.name} is now open.")
    
    def close_restaurant(self):
        self.open_status = False
        print(f"{self.name} is now closed.")
    
    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

# Example of creating an object
restaurant1 = Restaurant("Mama's Kitchen", "Italian")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.close_restaurant()

            

                