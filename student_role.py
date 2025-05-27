# Method Overriding with Method Resolution Order which determines the order in which
# base classes are searched when calling a method on a class instance, 
# especially when multiple inheritance is involved



class Person:
    def role(self):
        print("Just a person")

class Athlete(Person):
    def role(self):
        print("An athlete")  

class Artist(Person):
    def role(self):
        print("An Artist")

class Student(Artist,Athlete):
    pass

student =  Student()
student.role()
print(Student.__mro__)