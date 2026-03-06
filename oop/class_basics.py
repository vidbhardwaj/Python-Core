#class basics in python
class Student:
    #instance variables constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #method
    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
#make an object
s1 = Student("Vid", 20)
s2 = Student("XYZ", 22)
#calling
s1.show_info()
s2.show_info()