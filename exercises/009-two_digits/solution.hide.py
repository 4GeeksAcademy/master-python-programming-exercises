#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  aux = str(digit)
  return (int(aux[0]), int(aux[1]))
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
