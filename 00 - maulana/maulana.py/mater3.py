#mencari nilai maksimal
a=int(input('masukka anggka pertama : '))
b=int(input('masukkan angka kedua : '))
c=int(input('masukkan angka ketiga: '))
if a>b and a>c :
    nilaiMax=a
elif a<b and b>c :
    nilaiMax=b
else :
    nilaiMax=c
print('nilai max adalah = ' , nilaiMax)


#bilangan prima
print("menampilkan bilangan prima")
for a in range(2,100):
  for x in range(2,a):
    if (a%x == 0):
      break
    elif(a==89):
      break
  else:
     print(a)

#bilangan ganjil
print("menampilkan bilangan ganjil")
for i in range(3,100):
  for x in range(3,i):
    if (i%x == 0):
      break
    elif(i==89):
      break
    else:
      print(i)