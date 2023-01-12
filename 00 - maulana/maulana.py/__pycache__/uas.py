#2.2 mendapatkan nama hari dari suatu tanggal

days=('senin','selasa','rabu','kamis','jumat','sabtu','minggu')
num1=input('Masukkan informasi, hari pertama bulan ini, jatuh pada hari : ')
num2=int(input('masukkan tanggal yang ingin diketahui harinya : '))
for i in range (len(days)):
    if days[i]==num1:
        x=i-1
        y=(num2+x)%7
print('Tanggal', num2, 'adalah hari' , days[y])
