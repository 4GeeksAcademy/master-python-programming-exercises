# Your code here
def all_digits_even():
    lista = []
    for i in range(1000,3001):
        if i%2 ==0:
            lista.append(str(i))
    print(lista)
    return (lista)


all_digits_even()