# Your code here
def factorial(n):
    fact = 1
 
    for i in range(1, n+1):
        fact = fact * i

    return fact

print(factorial(8))

