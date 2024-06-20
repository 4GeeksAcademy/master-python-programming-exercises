# Your code here
def square_odd_numbers(text):
    result = []
    num = text.split(",")
    for i in num:
        if int(i)%2 != 0:
            result.append(int(i)**2) 
    return result
print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))