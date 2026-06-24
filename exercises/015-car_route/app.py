# Complete the function to return the amount of days it will take to cover a route
import math

def car_route(n,m):
  result = math.ceil (m / n)
  return result


# Invoke the function with two integers
print(car_route(30,90))
