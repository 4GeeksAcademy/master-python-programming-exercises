import math

# Complete the function to return the respective number of the century
def century(year):
  if year % 100 == 0:
    return math.floor(year / 100) 
  else:
    return math.floor(year / 100 + 1)


# Invoke the function with any given year
print(century(2024))
