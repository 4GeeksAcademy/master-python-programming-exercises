# `044` static and class methods

A **class method** is a method that is bound to the class and not the instance of the class. It takes the class itself as its first parameter, often named cls. Class methods are defined using the @classmethod decorator.

The primary characteristic of a class method is that it can access and modify class-level attributes, but it cannot access or modify instance-specific attributes since it doesn't have access to an instance of the class. Class methods are often used for tasks that involve the class itself rather than individual instances.

A **static method** in Python is a method that is bound to a class rather than an instance of the class. Unlike regular methods, static methods don't have access to the instance or class itself.

Static methods are often used when a particular method does not depend on the state of the instance or the class. They are more like utility functions associated with a class.

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

    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating instances of Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Using the class method to get the total number of people
total_people = Person.get_total_people()
print(f"Total People: {total_people}")

# Using the static method to check if a person is an adult
is_adult_person1 = Person.is_adult(person1.age)
is_adult_person2 = Person.is_adult(person2.age)
print(f"{person1.name} is an adult: {is_adult_person1}")
print(f"{person2.name} is an adult: {is_adult_person2}")
```        

In this example:

+ The class method `get_total_people` returns the total number of people created (instances of the Person class).

+ The static method `is_adult` checks if a person is an adult based on their age. It doesn't have access to instance or class variables directly.

## 📝 Instructions:

1. Create a class called `MathOperations`.

2. Inside the class, define the following:

+ A class variable named `pi` with a value of `3.14159`.
+ A class method named `calculate_circle_area` that takes a radius as a parameter and returns the area of a circle using the formula: `area = π × radius²`

3. Create a static method named `add_numbers` that takes two numbers as parameters and returns their sum.

4. Create an instance of the `MathOperations` class.

5. Use the class method `calculate_circle_area` to calculate the area of a circle with a radius of 5.

6. Use the static method `add_numbers` to add two numbers, for example, 10 and 15.

7. Print the results of each operation.

## 📎 Example input:

```py
math_operations_instance = MathOperations()
circle_area = MathOperations.calculate_circle_area(5)
sum_of_numbers = MathOperations.add_numbers(10, 15)
```

## 📎 Example output:

```py
# Circle Area: 78.53975
# Sum of Numbers: 25
```

## 💡 Hints:

+ Remember, to create a class method, use the `@classmethod` decorator above the method definition.

+ Remember, To create a static method, use the `@staticmethod` decorator above the method definition.

+ Anything you still don't fully get, we encourage you to always use the tools the internet provides you to search for information and clear most of your doubts (all developers do this don't worry).