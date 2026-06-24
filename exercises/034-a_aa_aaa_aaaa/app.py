# Your code here
def computed_value(num):
    valor = 0
    for i in range(1, 5):
         numero = int(str(num) * i)
         print("Numero", numero)
         valor += numero
         print("Valor", valor)
    return valor
    #return num + num*2 + num*111 + num*1111

print(computed_value(123))