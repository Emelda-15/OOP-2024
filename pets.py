class Pets:
    def __init__(self,name,color,age,size):
        self.name = name
        self.color = color
        self.age = age
        self.size = size
        
    def __str__(self): 
        return(f"name: {self.name} color: {self.color} age: {self.age} size: {self.size}")
            
        
pet1= Pets(f"dog", "white", 2, "small")
pet2= Pets(f"cat", "black", 3, "small")
pet3= Pets(f"donkey", "grey", 8, "big")
pet4= Pets(f"tiger", "brown", 6, "medium")
print(pet3)
        
        