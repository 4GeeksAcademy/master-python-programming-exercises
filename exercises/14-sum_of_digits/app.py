#Create two variables("num" and "total"). One variable will have any interger as its value,
#and the other will have the sum of the digits.

num = 3335
total=0

while(num>0):
    dig=num % 10
    total=total+dig
    num=num // 10
    
#print the sum of the digits

print(total)






  