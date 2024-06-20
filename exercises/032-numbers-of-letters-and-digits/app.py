# Your code here
def letters_and_digits(texto):
    valor = {"LETTERS": 0, "DIGITS": 0}
    for letra in texto:
        if letra.isalpha():
            valor['LETTERS'] += 1
        elif letra.isdigit():
            valor['DIGITS'] += 1
        else:
            pass

    return f"LETTERS {valor['LETTERS']} DIGITS {valor['DIGITS']}"


print(letters_and_digits("hello world! 123"))
