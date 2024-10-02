class Students:
    def __init__(self, name, address, year_of_entry):
        self.name = name
        self.address = address
        self.year_of_entry = year_of_entry

    def introduce(self):
        print(f"My name is {self.name} i stay at {self.address} and i joined in {self.year_of_entry} and my course is BSIT {self.course1}")
    
student1 =Students("Emelda", "Mukono", 2022)
student1.introduce()
print(student1)

class Course:
    def __init__(self, name, code, faculty):
        self.name = name
        self.code = code
        self.faculty= faculty
        
    def __str__(self):
        return(f"name: {self.name} code: {self.code} faculty: {self.faculty}")
    
course1 = Course("BSIT", 6, "COMPUTING")
print(course1)        
            
            
        