class Laptops:
    def __init__(self, name, color, storage):
        self.name = name
        self.color = color
        self.storage = storage
        
    def __str__(self):
        return(f"name: {self.name} color: {self.color} storage: {self.storage}")
    
laptop1 = Laptops("HP", "BLACK", '5GB')
laptop2 = Laptops("DELL", "BLUE", '4GB')
laptop3 = Laptops("TOSHIBA", "GREY", '8GB')
laptop4 = Laptops("NOTEBOOK", "WHITE", '10GB')

print(laptop4)    
            
        
        
        
        
        
        