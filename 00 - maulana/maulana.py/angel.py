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

def scanMat(val1, val2):
    matrix = []
    for i in range(len(val2[0])):
        jumlah = 0
        for j in range(len(val1)):
            temp = 0
            for k in range(len(val1[0])):
                temp += val1[j][k] * val2[i][k]
            jumlah += temp
        matrix.append(jumlah)
    return matrix

def addSparseMatrix2D(data1, data2) :
    baris1 = data1["baris"]
    kolom1 = data1["kolom"]
    baris2 = data2["baris"]
    kolom2 = data2["kolom"]
    addJumlah = {}
    mat1 = {}
    mat2 = {}
    for i in range(baris1) :
        for y in range(kolom1) :
            if (i,y) in data1 :
                nilai1 = data1[(i,y)]
                mat1[(i,y)] = nilai1
            else :
                mat1[(i,y)] = 0

    for i in range(baris2) :
        for y in range(kolom2) :
            if (i,y) in data2 :
                nilai2 = data2[(i,y)]
                mat2[(i,y)] = nilai2
            else :
                mat2[(i,y)] = 0


    if baris1 == baris2 and kolom1 == kolom2 :
        addJumlah["baris"] = baris1
        addJumlah["kolom"] = kolom1
        for i in range(baris1) :
            for y in range(kolom1) :
                if mat1[(i,y)] != 0 or mat2[(i,y)] != 0 :
                    nilai = mat1[(i,y)] + mat2[(i,y)]
                    addJumlah[(i,y)] = nilai
                else :
                    addJumlah[(i,y)] = 0
        return addJumlah
    else :
        return False


scanner = [[1, 0, -1], [0, -1, 0], [-1, 0, 1]]
mat = [[4, 2, 3, 1, 0], [7, 5, 6, 2, 1], [0, 0, 8, 7, 6], [9, 1, 1, 2, 7], [5, 6, 7, 0, 3]]

result = scanMat(scanner, mat)
print("Semangatt:v")
print(displayMatrix2D(scanner))
print(displayMatrix2D(mat))
print(displayMatrix2D(result))

import SparseMatrix as sm

print('Sparse Matriks 1:')
print(sm.dispplayMatrix2D(mat1))
print('Sparse Matriks 2:')
print(sm.dispplayMatrix2D(mat2))
hasilJumlah=sm.addSparseMatrix2D(mat1,mat2)
if hasilJumlah ==False:
    print('ukuran tidak sama')
else:
    print('hasil Penjumlahan:')
    print(sm.dispSparseMatrix2D(hasilJumlah))