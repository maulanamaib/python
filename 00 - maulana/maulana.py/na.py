#mencari nilai minimum
#d=int(input('masukkan nilai pertama : '))
##e=int(input('masukkan nilai kedua : '))
#f=int(input('masukkan nilai ketiga : '))
#g=int(input('masukkan nilai keempat: '))
#if d<e :
#    nilaiMin=d
#elif e>f :
#    nilaiMin=f
#elif f>g :
#    nilaiMin=g
#else :
#    nilaiMin=f
#print('nilai min adalah = ' ,nilaiMin)

stop=False
print("menu")
print("1. Tekan 1 untuk operasi perhitungan luas lingkaran")
print("2. Tekan 2 untuk operasi perhitungan luas persegi panjang")
print("3. Tekan 3 untuk operasi perhitungan luas segitiga")
tekan=input("masukkan pilihan anda=")
if tekan =='1':
  r=int(input('jarijari='))
  lL=22/7*r*r
  print(lL)
elif tekan == '2':
  p=int(input('panjang='))
  l=int(input('lebar='))
  lpp=p*l
  print(lpp)
elif tekan == '3':
  a=int(input('alas='))
  t=int(input('tinggi='))
  ls=1/2*a*t
  print(ls)
while not(stop):
  res=input('ingin mengulang oprasi kembali (y/t) ? ')
  if res=='y':
    tekan=input("masukkan pilihan anda=")
    if tekan =='1':
        r=int(input('jarijari='))
        lL=22/7*r*r
        print(lL)
    elif tekan == '2':
        p=int(input('panjang='))
        l=int(input('lebar='))
        lpp=p*l
        print(lpp)
    elif tekan == '3':
        a=int(input('alas='))
        t=int(input('tinggi='))
        ls=1/2*a*t
        print(ls)
  else:
    stop=True
