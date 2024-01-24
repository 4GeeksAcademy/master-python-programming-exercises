### DON'T modify this code ###

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours):
        return f"{self.name} is studying for {hours} hours."
        
### DON'T modify the code above ###
        
### ↓ Your code here ↓ ###

class CollegeStudent(Student):
    def __init__(self, name, age, grade, major):
        super().__init__(name, age, grade)
        self.major = major

    def introduce(self):
        return f"Hi there! I'm {self.name}, a college student majoring in {self.major}."

    def attend_lecture(self):
        return f"{self.name} is attending a lecture for {self.major} students."


college_student = CollegeStudent("Alice", 20, 90, "Computer Science")
print(college_student.introduce())
print(college_student.study(3))
print(college_student.attend_lecture())
