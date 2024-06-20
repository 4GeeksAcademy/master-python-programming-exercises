# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  result1 = 0
  for i in range(3):
    result = str(num)[i]
    result1 = result1 + int(result)
  return result1


# Invoke the function with any three-digit number
print(digits_sum(789))
