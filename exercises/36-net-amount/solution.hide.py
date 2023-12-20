# Your code here
def net_amount(param):
    total = 0
    values = param.split()
    for x in range(len(values)):
        if values[x] == 'D':
            total+=int(values[x+1])
        elif values[x] == 'W':
            total-=int(values[x+1])
    return total

print(net_amount("D 300 W 200 D 400"))
