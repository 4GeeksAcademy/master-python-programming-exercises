# Your code here
def list_and_tuple(*args):
    string_list = [str(num) for num in args]
    string_tuple = tuple(string_list)
    
    return string_list, string_tuple

result_list, result_tuple = list_and_tuple(1, 2, 3, 4, 5)
print(result_list)
print(result_tuple)
