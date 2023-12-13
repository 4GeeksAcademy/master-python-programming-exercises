# Your code here
def list_and_tuple(*nums):
    new_list = [str(num) for num in nums]
    new_tuple = tuple(new_list)
    
    return new_list, new_tuple


result_list, result_tuple = list_and_tuple(5, 4, 13, 24, 45)
print(result_list)
print(result_tuple)
