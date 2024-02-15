# `045` class methods

A **class method** is a method that is bound to the class and not the instance of the class. It takes the class itself as its first parameter, often named "cls". Class methods are defined using the @classmethod decorator.

The primary characteristic of a class method is that it can access and modify class-level attributes, but it cannot access or modify instance-specific attributes since it doesn't have access to an instance of the class. Class methods are often used for tasks that involve the class itself rather than individual instances.

```py
class Person:
    total_people = 0  # Class variable to keep track of the total number of people

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1  # Increment the total_people count for each new instance

    @classmethod
    def get_total_people(cls):
        return cls.total_people

# Creating instances of Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 16)

# Using the class method to get the total number of people
total_people = Person.get_total_people()
print(f"Total People: {total_people}")
```  

In this example:

+ The class method `get_total_people` returns the total number of people created (instances of the Person class).

## 📝 Instructions:

1. Create a class called `MathOperations`.

2. Inside the class, define the following:

+ A class variable named `pi` with a value of `3.14159`.
+ A class method named `calculate_circle_area` that takes a radius as a parameter and returns the area of a circle using the formula: `area = π × radius²`

3. Use the class method `calculate_circle_area` to calculate the area of a circle with a radius of 5.

4. Print the result. (No need to create any instance)

## 📎 Example input:

```py
circle_area = MathOperations.calculate_circle_area(5)
```

## 📎 Example output:

```py
# Circle Area: 78.53975
```


## 💡 Hints:

+ Remember, to create a class method, use the `@classmethod` decorator above the method definition.

+ Stuck? if you have any questions, reach out to your teachers, classmates, or use the Slack `#public-support-full-stack` channel to clear your doubts.

+ When you finish this exercise, add the `@staticmethod` from the previous exercise to your class and take your time to understand their differences and the reasons behind each one.