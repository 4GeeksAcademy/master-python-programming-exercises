# Complete the function to return the tens digit and the units digit of any interger
def two_digits(number):
    # Your code here
    aux = str(number)
    return (int(aux[0]), int(aux[1]))
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))


### SOLUTION 2 ###

# def two_digits(number):
#     tens_digit = number // 10
#     ones_digit = number % 10

#     return tens_digit, ones_digit

# print(two_digits(37))
