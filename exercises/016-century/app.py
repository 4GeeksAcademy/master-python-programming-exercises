# Complete the function to return the respective number of the century
import math
def century(year):
    if year % 100 == 0:
      return (year // 100) 
    else:
      return (year // 100 + 1)
  


# Invoke the function with any given year
print(century(1500))

