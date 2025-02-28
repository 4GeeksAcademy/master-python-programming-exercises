# Your code here
def factorial (n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(8))