# Your code here

class MathOperations:

    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2

math_operations_instance = MathOperations()
sum_of_numbers = MathOperations.add_numbers(10, 15)

print(f"Sum of Numbers: {sum_of_numbers}")