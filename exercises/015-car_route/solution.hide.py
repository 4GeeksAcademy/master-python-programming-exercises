import math

# Complete the function to return the amount of days it will take to cover a route
def car_route(n,m):
  return int(math.ceil(m/n))


# Invoke the function with two integers
print(car_route(35, 50))
