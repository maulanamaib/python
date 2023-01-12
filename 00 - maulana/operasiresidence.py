ListData=[]
def createList (x):
  for i in range(1,x+1):
    b=int(input('masukkan data ke - {} : '.format(i)))
    ListData.append(b)
  return ListData
def Persamaan1(data):
  count=0#22
  for i in data:
      count+=i #10+12+22
  size=count*1/i
  return size
def Persamaan2(data):
  coun=0
  cou=0
  for ch in data:
      coun+=ch
  siz=coun*1/ch
  for j in data:
      cou=cou+((j-siz)**2)
  si=cou*(1/(len(data)-1))
  return si


data=createList(7)
print('data list = ',data)
sigma1=Persamaan1(data)
print('Sigma nya (y) = ',sigma1)
sigma2=Persamaan2(data)
print('Sigma nya (z) = ',sigma2)


def createMatriks1D (x):
  Matriks1D=[]
  for i in range(x):
    b=int(input('masukkan data ke - {} : '.format(i)))
    Matriks1D.append(b)
  return Matriks1D
def addMatrix1D(matrx1,matrx2):
    if len(matrx1)!=len(matrx2):
        return 'Ukuran Matriks Tidak Sama'
    else:
        totalJumlah=[]
        for i in range(len(matrx1)): 
            totalJumlah.append(matrx1[i]+matrx2[i])
        return totalJumlah
def multiScalar(x, matrx) :
    hasilPerkalianSkalar = []
    for i in range(len(matrx)) : 
        hasilPerkalianSkalar.append(x*matrx[i])
    return hasilPerkalianSkalar  
def multiMatrix(matrix1,matrix2) :
    hasilPerkalianMatriks = []
    if len(matrix1)!=len(matrix2):
        return 'Ukuran Tidak Sama'
    else :
        for i in range(len(matrix1)) : 
            hasilPerkalianMatriks.append(matrix1[i]*matrix2[i])
        return hasilPerkalianMatriks 


data1=createMatriks1D(4)
print('Matriks 1D ke-1 = ',data1)
data2=createMatriks1D(3)
print('Matriks 1D ke-2 = ',data2)
data3=createMatriks1D(4)
print('Matriks 1D ke-3 = ',data3)

jumlah1 = addMatrix1D(data1, data2)
print("Matriks 1D ke-1 = ", data1)
print("Matriks 1D ke-2 = ", data2)
print("Hasil Penjumlahan = ", jumlah1)

jumlah2 = addMatrix1D(data1, data3)
print("Matriks 1D ke-1 = ", data1)
print("Matriks 1D ke-3 = ", data3)
print("Hasil Penjumlahan = ", jumlah2)

perkalian1=multiScalar(3, jumlah2)
print("Hasil Perkalian Skalar = ", perkalian1)

perkalian2=multiMatrix(perkalian1, data1)
print("Hasil Perkalian Matriks = ", perkalian2)


def createMatrix2D(baris , kolom) :
    matrix2D = []
    for i in range(1,baris+1) :
        Isi = []
        for j in range(1,kolom+1) :
            Isi.append(int(input('Matrix[%d,%d] = '%(i,j))))
        matrix2D.append(Isi)
    print(matrix2D)
    return matrix2D
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

def multiMatrix(matrx1, matrx2) :
    barisMatrx1 = len(matrx1)
    kolomMatrx1 = len(matrx1[0])
    barisMatrx2 = len(matrx2)
    kolomMatrx2 = len(matrx2[0])
    hasilPerkalian = []
    if kolomMatrx1 == barisMatrx2 :
        for i in range(barisMatrx1) :
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

data1 = createMatrix2D(2 , 3)
data2 = createMatrix2D(2 , 3)
data3 = createMatrix2D(2 , 2)

jumlah = addMatrix(data1, data2)
print("data 1 = ", data1)
print("data 2 = ", data2)
print("jumlah = ", jumlah)

jumlah = addMatrix(data1, data3)
print("data 1 = ", data1)
print("data 3 = ", data3)
print("jumlah = ", jumlah)

hasilKali = multiMatrix(data1, data2)
print("data 1 = ", data1)
print("data 2 = ", data2)
print("hasil perkalian = ", hasilKali)

hasilKali = multiMatrix(data1, data3)
print("hasil perkalian = ", hasilKali)

hasilKali = multiMatrix(data3, data2)
print("data 3 = ", data3)
print("data 2 = ", data2)
print("hasil perkalian = ", hasilKali)