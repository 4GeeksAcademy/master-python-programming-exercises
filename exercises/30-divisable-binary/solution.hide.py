# Your code here
def divisible_binary(binary_sequence):
    divisible_numbers = []
    binary_numbers = [x for x in binary_sequence.split(',')]
    for binary_num in binary_numbers:
        int_binary_num = int(binary_num, 2)
        if not int_binary_num % 5:
            divisible_numbers.append(binary_num)

    return ','.join(divisible_numbers)

print(divisible_binary("1000,1100,1010,1111"))
