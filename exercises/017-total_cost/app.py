# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    valor1 = d * n
    valor2 = c * n
    return valor1, valor2


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
