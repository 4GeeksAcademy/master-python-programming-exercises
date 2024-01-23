# `042` understanding classes

In Python, a class is a structure that allows you to organize and encapsulate related data and functionalities. Classes are a fundamental feature of object-oriented programming (OOP), a programming paradigm that uses objects to model and organize code.

In simple terms, a class is like a blueprint or a template for creating objects. An object is a specific instance of a class that has associated attributes (data) and methods (functions). Attributes represent the characteristics of the object, and methods represent the actions that the object can perform.

## 📎 Example:

```py
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
```

In this code: 

+ The `Student` class has an `__init__` method to initialize the attributes *name*, *age*, and *grade* of the student.
+ `introduce` is a method that prints a message introducing the student.
+ `study` is a method that simulates the act of studying and updates the student's grade.

## 📝 Instructions:

1. To complete this exercise, copy the provided code from the example and paste it into your `app.py` file. Execute the code and test its functionality. Experiment with modifying different aspects of the code to observe how it behaves. This hands-on approach will help you understand the structure and behavior of the `Student` class. Once you have familiarized yourself with the code and its effects, feel free to proceed to the next exercise.

## 💡 Hints:

+ Read about the `__init__` built-in function: https://www.w3schools.com/python/gloss_python_class_init.asp

+ If you find yourself wondering about the role of the `self` keyword in Python classes, take a moment to visit the following link for a detailed explanation: [Understanding the 'self' Parameter](https://www.geeksforgeeks.org/self-in-python-class/)
