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