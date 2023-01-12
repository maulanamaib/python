#bilangan prima
#print("masukkan bilangan prima, =")
#for a in range(2,100):
#  for x in range(2,a):
#    if (a%x == 0):
#      break
#  else:
#     print(a)

#data = [90, 56, 34, 78, 86, 90, 87, 88, 75, 65, 86, 57, 89, 67, 80]
#n=int(input('index='))
#for i in range(n):
#  if data<n:
#    data=i
#    print(i)
#bilangan=int(input('masukkan angka:'))
#bilfak=0
#faktor=[]
#i=1

#while i <=bilangan:
#    if (bilangan%i)==0:
#      bilfak+=1
#      faktor.append(i)
#    i+=1
#print('faktor pembagi dari',bilangan,'=',faktor)

hitung= True
while hitung :
    print('MENU :')
    print('tekan 0 untuk daftar mahasiswa. ')
    print('tekan 1 untuk rata rata nilai ')
    print('tekan 2 untuk daftar nilai mahasiswa yang lebih dari treshold')
    print('tekan 3 untuk nilai tertinggi')
    pil=int(input('Masukkan pilihan anda : '))
    if pil==0 :
        print('1. Manda = 90')
        print('2. lia = 80')
        print('3. Trias = 96')
        print('4. nova = 78')
        print('5. nina = 86')
        print('6. toy = 90')
    elif pil==1 :
        nilai=[90, 80, 96, 78, 86, 90]
        temp=0
        for i in nilai :
            temp+=i 
            rerata=temp/len(nilai)
        print('rata-rata nilai = ', rerata)
    elif pil==2 :
        nilai=[90, 80, 96, 78, 86, 90]
        th=int(input('masukkan batasan angka = '))
        maks=th
        for i in range(len(nilai)) :
            if th<nilai[i] :
                maks=nilai[i]
        print('indeks ke - ',i,'angkanya = ', maks)
    elif pil==3 :
        nilai=[90, 80,96, 78, 86, 90]
        maks=nilai[0]
        for i in range(1,len(nilai),1) :
            if maks<nilai[i] :
                maks=nilai[i]
        print(maks)
    else :
        print('-----------------------------------------------------------')
        print('Maaf, pilihan yang anda masukkan salah')

    again=True
    while again :
        lagi=input('Mencoba lagi?(ya/tidak) : ')
        if lagi =='ya' :
            again= False
            hitung= True
            print('-------------------------------------------------------')
        elif lagi == 'tidak' :
            again= False 
            hitung= False
            print('Selesai')
            print('Terimakasih telah menggunakan jasa kami.')
        else :
            print('------------------------------------------------------')
            print('Maaf, pilihan anda tidak sesuai')