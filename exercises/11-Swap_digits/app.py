#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  num = str(num)
  s = ""
  first_value = num[0]
  second_value = num[1]
  s+=second_value
  s+=first_value
  return s
  
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))