# Your code here
def squares_dictionary(n):
    sqr_dict = {}
    for i in range(1, n+1):
        sqr_dict[i]=i*i
    return sqr_dict

print(squares_dictionary(8))