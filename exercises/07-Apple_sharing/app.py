#Complete the function to print:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: Import the math module 
import math

def apple_sharing(n,k):

    print(math.floor(k / n))
    print(k % n)
    

#Print the two answer per the example output.
apple_sharing(6,50)