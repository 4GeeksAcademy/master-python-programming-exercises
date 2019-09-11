#Complete the fuction to print the swapped digits of a given two-digit-interger.
def swap_digits(num):
    first = num // 10
    second = num % 10
    swapped = (second * 10) + first
    print(swapped)
   
   
   
#Invoke the function with any two digit interger as its argument
swap_digits(101)

