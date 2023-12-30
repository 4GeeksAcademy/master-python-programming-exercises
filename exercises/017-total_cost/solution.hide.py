# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    total_cents = (d * 100 + c) * n
    total_dollars = total_cents // 100
    remaining_cents = total_cents % 100
    return total_dollars, remaining_cents


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
