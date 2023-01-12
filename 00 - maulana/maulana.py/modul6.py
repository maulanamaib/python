listdata=[]
listprima=[]
def createList (a):
  for i in range(0,a):
    b=int(input('masukkan data ke - {} :'.format(i)))
    listdata.append(b)
  return listdata

def isiPrime(a):
  count=0
  for y in range(1,a+1):
    if a%y==0:
      count+=1
  if count==2:
      for k in listprima:
        if a==k:
          break
      else:
        listprima.append(a)
      
def createlistprima(data):
  for i in data:
    isiPrime(i)
  return listprima


data=createList(10)
print('data list = ',data)
prima=createlistprima(data)
print('data prima = ',prima)



'Buatlah Fungsi dan code untuk memanggil fungsi dengan menggunakan Python, antara lain :'
'• Fungsi createList untuk membentuk suatu list dengan parameter atau argumen berupa ukuran list'
'• Fungsi avgList untuk menghitung rata-rata suatu list, dengan argumen adalah list'
'• Fungsi addList untuk menjumlahkan dua buah list yang memiliki ukuran yang sama)'


#2.2
def createList (a) :
    lst = []
    for i in range(a):
      x=int(input("Masukkan Data Ke {} : ".format(i)))
      lst.append(x)
    return lst
def avgList (data) :
    prim = len(data)
    ttl = 0
    for i in data :
      ttl+= i
    rata2 = ttl/prim
    return rata2

def addList (x , y) :
    prim1 = len(x)
    prim2 = len(y)
    total =[]
    if prim1 == prim2 :
        for i in range(prim1) :
          jumlah = x[i] + y[i]
          total.append(jumlah)
        return total
    else :
      return ("Ukuran List Tidak Sama")
 
data1 = createList(5)
print("data - 1 = " , data1 , " ; rata-rata list =", avgList(data1))
data2 = createList(5)
print("data - 2 = " , data2 , " ; rata-rata list =", avgList(data2))
hasil = addList(data1,data2)
print(data1 , "+" , data2 , "=" , hasil)