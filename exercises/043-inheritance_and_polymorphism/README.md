# `043` Inheritance and polymorphism

Now that we understand what a class is and some of its characteristics, let's talk about two new concepts related to classes: inheritance and polymorphism. Consider the following example:

```py
class HighSchoolStudent(Student):  # Add the parent class inside the parenthesis
    def __init__(self, name, age, grade, specialization):
        super().__init__(name, age, grade)
        self.specialization = specialization

    def study(self, hours):
        return f"{self.name} is a high school student specializing in {self.specialization} and is studying for {hours} hours for exams."

# Creating an instance of HighSchoolStudent
high_school_student = HighSchoolStudent("John", 16, 85, "Science")
print(high_school_student.introduce())  # We can call this method thanks to inheritance 
print(high_school_student.study(4))  # This method has been slightly modified and now it returns a different string
```

Assuming that the `Student` class from the previous exercise is coded just above this `HighSchoolStudent` class, to inherit its methods and attributes, we simply include the name of the class we want to inherit from (the parent class) inside the parentheses of the child class (`HighSchoolStudent`). As you can see, we can now use the `introduce` method from the `Student` class without having to code it again, making our code more efficient. The same applies to attributes; we don't need to redefine them.

Additionally, we have the flexibility to add new methods exclusively for this class or even override an inherited method if needed, as demonstrated in the `study` method, which is slightly modified from the `Student` method; this is called **polymorphism**.

## 📝 Instructions:

1. Create a class called `CollegeStudent` which inherits from the already defined `Student` class.

2. Add a new attribute called `major` to represent the major they are studying.

3. Modify the inherited `introduce` method to return this string:

```py
"Hi there! I'm <name>, a college student majoring in <major>."
```

4. Add a new method called `attend_lecture` that returns the following string:

```py
"<name> is attending a lecture for <major> students."
```

5. Create an instance of your newly created class and call each of its methods. Execute your code to ensure it works.

## 💡 Hint:

+ You may have noticed the use of a new method `super()` which is necessary for inheriting from a parent class. Take a look at where it is positioned and have a read about it: [Understanding Python's super()](https://realpython.com/python-super/).
