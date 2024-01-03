# Your code here

class MathOperations:
    pi = 3.14159

    @classmethod
    def calculate_circle_area(cls, radius):
        area = cls.pi * radius ** 2
        return area

    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2


math_operations_instance = MathOperations()
circle_area = MathOperations.calculate_circle_area(5)
sum_of_numbers = MathOperations.add_numbers(10, 15)


print(f"Circle Area: {circle_area}")
print(f"Sum of Numbers: {sum_of_numbers}")