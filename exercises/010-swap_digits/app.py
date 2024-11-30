# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  result = str(num % 10 ) + str(num // 10)
  return int(result)
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
