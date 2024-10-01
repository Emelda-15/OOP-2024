class University:
    def __init__(self, name, location, motto, branches = 1):
        self.name = name
        self.location = location
        self.motto = motto
        self.branches = branches
        
    def __str__(self):
        return(f"Name: {self.name} location: {self.location} motto: {self.motto} branches: {self.branches}") 
        
University1 = University("Uganda Christian University", "Mukono", "Centre of Excellence in the heart of East Africa") 
University2 = University("KYU", "Kireka", "DO DAT", 4) 
University3 = University("MUK", "Kampala", "HERE WE ARE", 2) 
  
print(University3) 
          
    
     
        
        
        