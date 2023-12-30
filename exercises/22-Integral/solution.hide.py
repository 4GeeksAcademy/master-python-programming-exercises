# Your code here
def squares_dictionary(n):
    new_dict = dict()
    for i in range(1, n + 1):
        new_dict[i] = i * i
    return new_dict

print(squares_dictionary(5))
