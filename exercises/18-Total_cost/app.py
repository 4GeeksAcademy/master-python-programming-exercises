#Complete the function to print the total cost in dollars and cents of N cupcakes. 
def total_cost(d,c,n):

    sum1=((d*100)+c)
    sum2=(sum1*n)
    dollar2=(sum2//100)
    cent2=(sum2%100)
    print("%i %i" % (dollar2,cent2))



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.

