#Create two variables("num" and "total"). One variable will have any interger as its value,
#and the other will have the sum of the digits.

num=int(1234)
total=0
while(num>0):
    dig=num%10
    total=total+dig
    num=num//10

#print the sum of the digits
print("The total sum of digits is:",total)







  