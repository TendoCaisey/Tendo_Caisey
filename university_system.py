class Person:
    def __init__(self,name , age , university_id):
        self.name = name
        self.age = age
        self.university_id = university_id

    def display_info(self):
        print(f"Name :{self.name}")   
        print(f"Age :{self.age}")  
        print(f"University_id : {self.university_id}")  

class Student(Person):
    def __init__(self, name, age, university_id,course, year):
        super().__init__(name, age, university_id) 
        self.course = course
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Role: Student")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")

class Lecturer(Person):
    def __init__(self, name, age, university_id,departments,subjects,):
        super().__init__(name, age, university_id) 
        self.departments = departments
        self.subjects = subjects

    def display_info(self):
        super().display_info()
        print(f"Role : Lecturer")
        print(f"Department: {self.departments}")
        print(f"Subjects : {', '.join(self.subjects)}") 

class Staff(Person):
    def __init__(self, name, age, university_id, position, office):
        super().__init__(name, age, university_id)
        self.position = position
        self.office = office

    def display_info(self):
        super().display_info()
        print(f"Role: Staff")
        print(f"Position: {self.position}")
        print(f"Office: {self.office}")


print("=== Student Info ===")
s1 = Student("Tendo Caisey",21,"23789609","BSSE",2023)
s1.display_info()

print("\n=== Lecturer Info ===")
l1 = Lecturer("Dr. jeff", 38, "L456", "Networks", ["Data Analysis", "Machine Learning"])
l1.display_info()

print("\n=== Staff Info ===")
st1 = Staff("Mr. Smith", 38, "T789", "Technician", "big lab 2")
st1.display_info()
    

        