def two_dimensional_array(nList, nElements):
    dimensions=[int(x) for x in "{},{}".format(nList,nElements).split(',')]
    rowNum=dimensions[0]
    colNum=dimensions[1]
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= row*col

    return (multilist)
