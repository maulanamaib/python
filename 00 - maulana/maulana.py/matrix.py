

#2.1 
def createMatrix2D(baris, kolom) :
    matrix2D = []
    for i in range(1,baris+1) :
        List = []
        for j in range(1,kolom+1) :
            List.append(int(input('Matrix[%d,%d] = '%(i,j))))
        matrix2D.append(List)
    print(matrix2D)
    return matrix2D

#2.2 
def displayMatrix(data):
    totalBaris=len(data)
    totalKolom=len(data[0])
    mat=''
    for i in range(totalBaris):
        num=''
        for j in range(totalKolom):
            num=num+' '+str('%4d'%data[i][j])
        num='%4s'%'|'+num+'%4s'%'|'
        mat=mat+num+'\n'
    return (mat)

#2.3
def isSquare(matrx) :
    if len(matrx) == len(matrx[0]) :
        return True
    else :
        return False

#2.4 
def addMatrix(matrx1,matrx2):
    if len(matrx1)!=len(matrx2) or len(matrx1[0])!=len(matrx2[0]):
        return 'Ukuran Tidak Sama'
    else:
        totalJumlah=[]
        for i in range(len(matrx1)): 
            num=[]
            for j in range(len(matrx1[0])):
                num.append(matrx1[i][j]+matrx2[i][j])
            totalJumlah.append(num)
        return totalJumlah
#2.5
def multiMatrix(matrx1, matrx2) :
    barisMatrx1 = len(matrx1)
    kolomMatrx1 = len(matrx1[0])
    barisMatrx2 = len(matrx2)
    kolomMatrx2 = len(matrx2[0])
    hasilPerkalian = []
    if kolomMatrx1 == barisMatrx2 :
        for i in range(i) :
            kolomKali = []
            for k in range(kolomMatrx2) :
                temp = 0
                for j in range(kolomMatrx1) :
                    temp=temp+matrx1[i][j]*matrx2[j][k]
                kolomKali.append(temp) 
            hasilPerkalian.append(kolomKali)
        return hasilPerkalian
    else:
        return 'ukuran tidak sama'

#2.6
def maksMat(matrx, BdanK) :
    baris = []
    if BdanK == "baris" :
        indeks = 0
        for i in matrx :
            baris = []
            max = matrx[indeks][0]
            for BdanK in i :
                if BdanK > max :
                    max = BdanK
            baris.append(max)
            baris.append(baris)
            indeks += 1
        return baris
    elif BdanK == "kolom" :
        kolom = []
        for BdanK in range(len(matrx[0])) :
            max = matrx[0][BdanK]
            for i in range(len(matrx)) :
                if matrx[i][BdanK] > max :
                    max = matrx[i][BdanK]
            kolom.append(max)
        baris.append(kolom)
        return baris
    elif BatauK == "*" :
        max = matrx[0][0]
        for i in matrx :
            for BatauK in i :
                if BatauK > max :
                    max = BatauK
        return max


import matrix

#2.1
data1 = matrix.createMatrix2D(3, 3)
data2 = matrix.createMatrix2D(3, 3)
data3 = matrix.createMatrix2D(1, 3)
data4 = matrix.createMatrix2D(3, 1)

import matrix

#2.2
print("data 1 = ", matrix.displayMatrix(data1), sep = "\n")
print("data 2 = ", matrix.displayMatrix(data2), sep = "\n")
print("data 3 = ", matrix.displayMatrix(data3), sep = "\n")
print("data 4 = ", matrix.displayMatrix(data4), sep = "\n")


import matrix

#2.3
print("data 1 = ", matrix.displayMatrix(data1), sep = "\n")
print("is square ? ", matrix.isSquare(data1), "\n")
print("data 2 = ", matrix.displayMatrix(data2), sep = "\n")
print("is square ? ", matrix.isSquare(data2), "\n")
print("data 3 = ", matrix.displayMatrix(data3), sep = "\n")
print("is square ? ", matrix.isSquare(data3), "\n")
print("data 4 = ", matrix.displayMatrix(data4), sep = "\n")
print("is square ? ", matrix.isSquare(data4), "\n")


import matrix

#2.4
jumlah = matrix.addMatrix(data1, data2)
print("data 1 = ", matrix.displayMatrix(data1), sep = "\n")
print("data 2 = ", matrix.displayMatrix(data2), sep = "\n")
print("jumlah = ", matrix.displayMatrix(jumlah), sep = "\n")

jumlah = matrix.addMatrix(data1, data3)
print("data 1 = ", matrix.displayMatrix(data1), sep = "\n")
print("data 3 = ", matrix.displayMatrix(data3), sep = "\n")
print(jumlah)


import matrix

#2.5
hasilKali = matrix.multiMatrix(data1, data2)
print("data 1 = ", matrix.displayMatrix(data1), sep = "\n")
print("data 2 = ", matrix.displayMatrix(data2), sep = "\n")
print("hasil perkalian = ", matrix.displayMatrix(hasilKali), sep = "\n")

hasilKali = matrix.multiMatrix(data1, data3)
print(hasilKali)

hasilKali = matrix.multiMatrix(data3, data4)
print("data 3 = ", matrix.displayMatrix(data3), sep = "\n")
print("data 4 = ", matrix.displayMatrix(data4), sep = "\n")
print("hasil perkalian = ", matrix.displayMatrix(hasilKali), sep = "\n")



import matrix

#2.6
maksBaris = matrix.maksMat(data1, 'baris')
maksKolom = matrix.maksMat(data1, 'kolom')
maks = matrix.maksMat(data1, '*')
print("data 1 = ", matrix.displayMatrix(data1), sep = "\n")
print("maksimum baris = ", matrix.displayMatrix(maksBaris), sep = "\n")
print("maksimum kolom = ", matrix.displayMatrix(maksKolom), sep = "\n")
print("maksimum = ", maks)