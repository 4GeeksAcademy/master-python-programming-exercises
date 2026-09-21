# Your code here
def list_and_tuple(*args):
    lista = []
    for arg in args:
        lista.append(str(arg))
    tupla = tuple(lista)
    return lista, tupla

list_and_tuple(34,67,55,33,12,98,33,4555,6777,0,88)