class Shape:
    def __init__(self,type,sides):
     self.type =type
     self.sides = sides
    def area(self):
        print(f"{type}'s area is")
        
        
class Square(Shape):
    def __init__(self, type, sides, length):
        super().__init__(type, sides)
        self.length = length

    def area(self):
        print(f"Area = {self.length ** 2}")  
        
Square = Square("square", 6, 6)
Square.area()

class Rectangle(Shape):
    def __init__(self, type, sides, length, width):
        super().__init__(type, sides)
        self.width = width
        
    def are(self):
        print(f"Area = {self.length * self.width}")   
        
Rectangle = Rectangle(Rectangle, 4, 5, 7)
Rectangle.area()         
            

        
              
    