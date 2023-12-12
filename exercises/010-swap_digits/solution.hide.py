# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  aux = str(num)[1] + str(num)[0]
  return int(aux)
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
