# Complete the function to return the total cost in dollars and cents of (n) cupcakes
import math

def total_cost(d, c, n):
    dollars = n*d
    cents = n*c
    if cents >= 100:
        dollars += math.floor(cents/100)
        cents = cents%100
    return (dollars, cents)


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
