class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade
    def display(self):
        print(f"{self.sid} | {self.name} | {self.grade}")
class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def remove_student(self, sid):
        self.students = [s for s in self.students if s.sid != sid]
    def find_student(self, sid):
        for s in self.students:
            if s.sid == sid:
                return s
        return None
    def show_all(self):
        for s in self.students:
            s.display()
def main():
    sm = StudentManager()
    sm.add_student(Student(1, "Vid", 85.5))
    sm.add_student(Student(2, "abc", 90.0))
    sm.add_student(Student(3, "xyz", 78.2))
    print("All Students:")
    sm.show_all()
    print("\nSearching ID 2:")
    s = sm.find_student(2)
    if s: s.display()
    print("\nRemoving ID 3...")
    sm.remove_student(3)
    sm.show_all()
if __name__ == "__main__":
    main()