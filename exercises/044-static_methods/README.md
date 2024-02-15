# `044` static methods

A **static method** in Python is a method that is bound to a class rather than an instance of the class. Unlike regular methods, static methods don't have access to the instance or class itself.

Static methods are often used when a particular method does not depend on the state of the instance or the class. They are more like utility functions associated with a class.

```py
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating instances of Person
person1 = Person("Alice", 25)
person2 = Person("Bob", 16)

# Using the static method to check if a person is an adult
is_adult_person1 = Person.is_adult(person1.age)
is_adult_person2 = Person.is_adult(person2.age)
print(f"{person1.name} is an adult: {is_adult_person1}")
print(f"{person2.name} is an adult: {is_adult_person2}")
```        

In this example:

+ The static method `is_adult` checks if a person is an adult based on their age. It doesn't have access to instance or class variables directly.

## 📝 Instructions:

1. Create a class called `MathOperations`.

2. Create a static method named `add_numbers` that takes two numbers as parameters and returns their sum.

3. Create an instance of the `MathOperations` class.

4. Use the static method `add_numbers` to add two numbers, for example, 10 and 15.

5. Print the result.

## 📎 Example input:

```py
math_operations_instance = MathOperations()
sum_of_numbers = MathOperations.add_numbers(10, 15)
```

## 📎 Example output:

```py
# Sum of Numbers: 25
```

## 💡 Hints:

+ Remember, To create a static method, use the `@staticmethod` decorator above the method definition.

+ For anything you still don't fully get, we encourage you to always use the tools the internet provides you to search for information and clear most of your doubts (all developers do this, don't worry).
