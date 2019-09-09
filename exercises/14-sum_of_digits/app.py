

#Finish the function to find the sum of the digits:
def digits_sum(digit):
    num = digit
    total = 0
    while(num>0):
        dig = num % 10
        total = total + dig
        num = num // 10
    print(total)

digits_sum(1234)




