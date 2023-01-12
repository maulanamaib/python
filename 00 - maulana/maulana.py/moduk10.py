print('Sparse Matriks 1:')
print(sm.dispSparseMatrix2D(mat1))
print('Sparse Matriks 2:')
print(sm.dispSparseMatrix2D(mat2))
hasilJumlah=sm.addSparseMatrix2D(mat1,mat2)
if hasilJumlah ==False:
    print('ukuran tidak sama')
else:
    print('hasil Penjumlahan:')
    print(sm.dispSparseMarix2D(hasilJumlah))