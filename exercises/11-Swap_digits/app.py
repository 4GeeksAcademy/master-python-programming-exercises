#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  result = str(num%10)+str(num//10)
  return (result)
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(76))


