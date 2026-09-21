# Your code here
def number_of_uppercase(texto):
    valor = {"UPPERCASE": 0, "LOWERCASE": 0}
    for letra in texto:
        if letra.islower()  and letra.isalpha():
            valor['LOWERCASE'] += 1
        elif letra.isupper() and letra.isalpha():
            valor['UPPERCASE'] += 1


    return f"UPPERCASE {valor['UPPERCASE']} LOWERCASE {valor['LOWERCASE']}"


print(number_of_uppercase("Hello world!"))