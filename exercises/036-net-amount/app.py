# Your code here
def net_amount(entrada):
    result = 0
    valor = entrada.split(" ")

    for i in range(len(valor)):
        if valor[i] == "D":
            result += int(valor[i+1])
        elif valor[i] == "W":
            result -= int(valor[i+1])

    return result

net_amount("D 300 D 300 W 200 D 100")

