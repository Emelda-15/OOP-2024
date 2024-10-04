class Dog:
    species = "Canine"  # Class variable
    
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable

# Creating two objects
dog1 = Dog("Buddy", 5)
dog2 = Dog("Bella", 3)

print(dog1.species)  # Output: Canine (class variable, same for all)
print(dog2.species)  # Output: Canine
print(dog1.name)     # Output: Buddy (instance variable, unique to dog1)
print(dog2.name)     # Output: Bella (instance variable, unique to dog2)
