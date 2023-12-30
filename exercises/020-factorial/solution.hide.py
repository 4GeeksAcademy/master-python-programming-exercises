# Your code here
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

print(factorial(5))

### Solution 2 ###

# import math
#
# def factorial(x):
#     return math.factorial(x)
#
# print(factorial(8))
