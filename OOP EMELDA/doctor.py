class Doctor:
    def __init__(self, name, specialization, years_of_experience):
        self.name = name
        self.specialization = specialization
        self.years_of_experience = years_of_experience
    
    def treat_patient(self, patient_name):
        print(f"Dr. {self.name} is treating {patient_name}.")
    
    def get_info(self):
        print(f"Dr. {self.name} specializes in {self.specialization} with {self.years_of_experience} years of experience.")

# Example of creating an object
doctor1 = Doctor("Ritah", "Pediatrics", 10)
doctor1.get_info()
doctor1.treat_patient("Mercy")
