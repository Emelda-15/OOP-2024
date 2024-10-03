class School:
    def __init__(self, name, location, num_students, num_teachers):
        self.name = name
        self.location = location
        self.num_students = num_students
        self.num_teachers = num_teachers

    def student_teacher_ratio(self):
        if self.num_teachers == 0:  # Avoid division by zero
            return "No teachers available."
        return self.num_students / self.num_teachers

    def school_info(self):
        return f"School Name: {self.name}\nLocation: {self.location}\nNumber of Students: {self.num_students}\nNumber of Teachers: {self.num_teachers}\n"

# Creating sample objects
school1 = School("Greenwood High", "New York", 500, 25)
school2 = School("Sunrise Academy", "Los Angeles", 800, 40)

# Accessing object data
print(school1.school_info())
print(f"Student-Teacher Ratio: {school1.student_teacher_ratio()}\n")

print(school2.school_info())
print(f"Student-Teacher Ratio: {school2.student_teacher_ratio()}")
