print("=== Demonstration of class / blueprint ===")

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"

student = Student("John", 20, 85)
print(student)  