# Your code here
def all_digits_even():
    values = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            values.append(s)

    return ",".join(values)

print(all_digits_even())
