class DivisibleBySevenIterator:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for number in range(self.n + 1):
            if number % 7 == 0:
                yield number


n_value = 50
divisible_by_seven_iterator = DivisibleBySevenIterator(n_value)

for num in divisible_by_seven_iterator.generate_divisible_by_seven():
    print(num)
