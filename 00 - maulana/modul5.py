#2.1
data1 = []
nilai = []
jmlh1 = int(input('masukan ukuran list yang pertama = '))
for i in range (jmlh1):
  pret1='masukan data ke-'+str(i)+':'
  a=int(input(pret1))
  data1.append(a)

data2 = []
jmlh2 = int(input('masukan ukuran list yang kedua = '))
for i in range (jmlh2):
  pret2='masukan data ke-'+str(i)+':'
  b=int(input(pret2))
  data2.append(b)

tambah=[]
if len(data1)>len(data2):
    for i in range (jmlh2):
        c=data2[i]+data1[i]
        tambah.append(c)
    for i in range (jmlh2,jmlh1):
        tambah.append(data1[i])
else:
    for i in range (jmlh1):
        c=data1[i]+data2[i]
        tambah.append(c)
    for i in range (jmlh1,jmlh2):
        tambah.append(data2[i])
print("list pertama : ",data1)
print("list kedua : ",data2)
print("Hasil penjumlahan = ",tambah)


#2.2 mendapatkan nama hari dari suatu tanggal

days=('senin','selasa','rabu','kamis','jumat','sabtu','minggu')
num1=input('Masukkan informasi, hari pertama bulan ini, jatuh pada hari : ')
num2=int(input('masukkan tanggal yang ingin diketahui harinya : '))
for i in range (len(days)):
    if days[i]==num1:
        x=i-1
        y=(num2+x)%7
print('Tanggal', num2, 'adalah hari' , days[y])




#2.3 
List = []
jumlah = int(input('masukan ukuran list yang pertama = '))
for n in range (jumlah):
  hasil='masukan data ke-'+str(n)+':'
  a=int(input(hasil))
  List.append(a)

ganjil=[i for i in List if i%2==1]
genap=[i for i in List if i%2==0 ]
print(List)
print(ganjil)
print(genap)