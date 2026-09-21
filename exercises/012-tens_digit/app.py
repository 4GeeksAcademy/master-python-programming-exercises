# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  result = str(num)[-2]
  return int(result)


# Invoke the function with any integer
print(tens_digit(179))
