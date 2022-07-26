def net_amount(param):
    netAmount = 0
    values = param.split()
    for x in range(len(values)):
        if values[x] == 'D':
            netAmount+=int(values[x+1])
        elif values[x] == 'W':
            netAmount-=int(values[x+1])
    return netAmount
