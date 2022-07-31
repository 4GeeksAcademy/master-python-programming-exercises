def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print (fact(x))


# or

# Your code here
import math
def factorial(num):
    return math.factorial(num)

print(factorial(8))