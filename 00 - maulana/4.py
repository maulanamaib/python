#bilangan=int(input('masukkan angka:'))
#counter=0
#for i in range(bilangan):
#  if (bilangan%(i+1)==0):
#    counter+=1
#if counter==2:
#  print('bilangan prima')
#else:
#  print(bilangan,'bukan prima' ,bilangan, 'memiliki jumlah faktor pembagi',counter)


#n=int(input('masukkan jumlah bilangan : '))
#y=1
#for i in range(n):
# if i%2=0:
#   print(i)
#   y = y + i
#print('total penjumlahan semuua bilangan adalah: ', y)


stop=False
while not(stop):
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
  else:
    a=int(input('alas='))
    t=int(input('tinggi='))
    ls=1/2*a*t
    print(ls)
  res=input('ingin mengulang oprasi kembali (y/t) ? ')
  if res=='t':
    stop=True
while again :
        lagi=input('Mencoba lagi?(ya/tidak) : ')
        if lagi =='ya' :
            again= False
            hitung= True 
        elif lagi == 'tidak' :
            again= False 
            hitung= False
            print('Selesai')
            print('Terimakasih telah menggunakan jasa kami.')
        else :
            print('Maaf, pilihan anda tidak sesuai')
