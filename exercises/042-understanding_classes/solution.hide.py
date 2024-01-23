# Your code here
class Student:
    def __init__(self, name, age, grade): # These are its attributes
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self): # This is a method
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours): # This is another method
        self.grade += hours * 0.5
        return f"After studying for {hours} hours, {self.name}'s new grade is {self.grade}."

student1 = Student("Ana", 20, 80)

print(student1.introduce())
print(student1.study(3))
