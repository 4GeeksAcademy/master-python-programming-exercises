# `042.1` `__init__` and `__str__` methods

Typically, when working with classes, you will encounter methods of the form `__<method>__`; these are known as "magic methods." There are a lot of them, each serving a specific purpose. This time, we will focus on learning two of the most fundamental ones.

The magic method `__init__` is essential for the initialization of objects within a class. It is automatically executed when a new instance of the class is created, allowing for the assignment of initial values to the object's attributes.

The `__str__` method is used to provide a readable string representation of the instance, allowing customization of the output when the object is printed. This is especially useful for improving code readability and facilitating debugging, as it defines a human-friendly version of the information contained in the object.

## 📎 Example:

```py
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.gender}"

# Create an instance of the Person class
person1 = Person("Juan", 25, "Male")

# Print the information of the person using the __str__ method
print(person1)  # Output: Juan, 25 years old, Male
```

## 📝 Instructions:

1. Create a class called `Book` that has the `__init__` and `__str__` methods.

2. The `__init__` method should initialize the `title`, `author`, and `year` attributes.

3. The `__str__` method should return a string representing the information of an instance of the following book in this manner:

```py
book1 = ("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(book1)

# Output:
#
# Book Title: The Great Gatsby
# Author: F. Scott Fitzgerald
# Year: 1925
```

## 💡 Hints:

+ Use the `__init__` method to initialize the instance's attributes.

+ Use the `__str__` method to provide a readable string representation of the instance.

+ To create line breaks within a string, you can use the `\n` characters.