import math

# Complete the function to return the first digit to the right of the decimal point
def first_digit(num):
  return int(str(math.floor(num*10)/10)[-1])


# Invoke the function with a positive real number. ex. 34.33
print(first_digit(2.6))
