# Your code here
def square_odd_numbers(numbers):
    number_list = [int(num) for num in numbers.split(',')]
    squared_odd_numbers = [num**2 for num in number_list if num % 2 != 0]

    return squared_odd_numbers

print(square_odd_numbers("1,2,3,4,5,6,7"))
