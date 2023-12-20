# Your code here
def letters_and_digits(text):
    counts = {"DIGITS": 0, "LETTERS": 0}
    for char in text:
        if char.isdigit():
            counts["DIGITS"] += 1
        elif char.isalpha():
            counts["LETTERS"] += 1
        else:
            pass
    
    return f"LETTERS {counts['LETTERS']} DIGITS {counts['DIGITS']}"

print(letters_and_digits("hello world! 123"))
