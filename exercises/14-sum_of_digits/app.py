#Create one variable ("three_digit_number") and give any three digits interger as its value,
three_digit_number = 454

#Finish the function to find the sum of the digits:
def digits_sum(digit):
    num = digit
    total = 0
    while(num>0):
        dig = num % 10
        total = total + dig
        num = num // 10
    print(total)
    

#DO NOT CHANGE!
digits_sum(three_digit_number)




