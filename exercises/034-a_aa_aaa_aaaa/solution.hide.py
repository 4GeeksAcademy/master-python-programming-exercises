# Your code here
def computed_value(param):
    result = 0
    for i in range(1, 5):
        concatenated_number = int(str(param) * i)
        result += concatenated_number
    return result

print(computed_value(9))
