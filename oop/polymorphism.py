#polymorphism in python
class dog:
    def sound(self):
        print("dog barks")
class cat:
    def sound(self):
        print("cat meows")
class cow:
    def sound(self):
        print("cow moos")
#polymorphism
animals = [dog(), cat(), cow()]
for a in animals:
    a.sound()