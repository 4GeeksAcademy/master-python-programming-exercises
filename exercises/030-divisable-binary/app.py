# Your code here
def divisible_binary(binary_):
    bin_ = binary_.split(",")
    lista =[]
    for i in bin_:
        if int(i,2)%5 == 0:
            lista.append(i)
    return ",".join(lista)

print(divisible_binary("1010,1010,1010,1010"))