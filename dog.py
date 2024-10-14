class Dog:
    # Constructor (Initializer)
    def __init__(self, name, breed, age):
        self.name = name  
        self.breed = breed 
        self.age = age  
        
    def play(self):
          print(f"The dog is playing")
        
    def show(self):
            print(f"Name: {self.name}")
            print(f"Breed: {self.breed}")
            
Dave =Dog("Dave", "maltiz", "female")
Dave.show()
            
    
    
