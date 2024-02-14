# `030` Divisable binary

## 📝 Instructions:

1. Write a function `divisible_binary()` that takes a sequence of comma-separated 4-digit binary numbers as input and checks if they are divisible by 5. Print the numbers that are divisible by 5 in a comma-separated sequence.

## 📎 Example input:

```py
divisible_binary("0100,0011,1010,1001")
```

## 📎 Example output:

```py
1010
```

## 💡 Hint:

+ To convert binary numbers into our everyday integer numbers (base 10 or decimal), you have to include the base of the number we input in the first argument (in this case, base 2 or binary), and the function `int()` will take care of the rest. Like this:

```py
binary = '0101'
decimal = int(binary, 2)

print(decimal)  # Output: 5
```
