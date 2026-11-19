# Your code here
def two_dimensional_list(x,y):
    matriz_final = []
    for i in range(x):
        matriz = []
        for j in range(y):
            matriz.append(i*j)
        matriz_final.append(matriz)
    return matriz_final

two_dimensional_list(3,5)