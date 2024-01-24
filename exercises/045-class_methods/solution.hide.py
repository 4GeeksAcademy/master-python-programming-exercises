# Your code here

class MathOperations:
    pi = 3.14159

    @classmethod
    def calculate_circle_area(cls, radius):
        area = cls.pi * radius ** 2
        return area

circle_area = MathOperations.calculate_circle_area(5)

print(f"Circle Area: {circle_area}")