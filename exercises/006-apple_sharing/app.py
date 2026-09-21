def apple_sharing(n,k):
  # Your code here
  result =  k // n
  resto = k % n
  return result,resto
 

print(apple_sharing(6,50))
