# Defining a class called Person
class Person:
    # Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Attribute for person's name
        self.age = age    # Attribute for person's age

    # Method to display person's details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object (instance) of the class Person
person1 = Person("Jonah", 30)

# Calling the method to display the object's details
person1.display_info()
