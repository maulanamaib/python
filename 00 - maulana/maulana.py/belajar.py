def displayMatrix2D(value):
    sumRows = len(value)
    sumCols = len(value[0])
    showMatrix = ''
    for i in range(sumRows):
        dispTemp = ''
        for j in range(sumCols):
            dispTemp += f"  {str(value[i][j])}   "
        showMatrix += f"| {dispTemp} |\n"
    return showMatrix

def multMat(val1, val2):
    showMultResults = []
    for i in range(len(val1)):
        for j in range(len(val2[0])):
            multTemp = 0
            multResults = []
            for k in range(len(val1[0])):
                multTemp += val1[i][k] * val2[k][j]
            multResults.append(multTemp)
        showMultResults.append(multResults)
    return showMultResults


scanner = [[1, 0, -1], [0, -1, 0], [-1, 0, 1]]
mat = [[4, 2, 3, 1, 0], [7, 5, 6, 2, 1], [0, 0, 8, 7, 6], [9, 1, 1, 2, 7], [5, 6, 7, 0, 3]]

result = multMat(scanner, mat)
print("Semangatt:v \n")
print(displayMatrix2D(scanner))
print(displayMatrix2D(mat))
print(displayMatrix2D(result))