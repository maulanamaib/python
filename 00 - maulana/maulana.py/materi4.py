#temp=0
#n=int(input('masukkan angka:'))
#for i in range(n):
#    if i%2==1:
#        temp=temp+i
#        print('bilangan ke-','=',i)
#print('total angka:', temp) 

#num1=1
#num2=1
#temp=1
#n=int(input('masukkan jumlah bilangan='))
#for i in range(n):
#  varb=num1+num2
#  print(varb)
#  num1=num2
#  num2=varb
#  temp=temp+varb
#print('total penjumlahan semua bilangan adalah=',temp)

#tugas 2.1
num1=0
nm1=" "
num2=0
nm2=" "
num3=0
nm3=" "
l=str(input('masukkan kalimat= '))
for i in l:
  if i=='a' or i=='i' or i=='u' or i=='e' or i=='o' or i=='A' or i=='I' or i=='U' or i=='E' or i=='O':
    num1=num1+1
    nm1=nm1+i
    nm1=nm1+" "
  elif i==" ":
    num2+=1
    nm2=nm2+i
  else:
    num3=num3+1
    nm3=nm3+i
    nm3=nm3+" " 
print('jumlah huruf vocal=',num1, '=',nm1)
print('jumlah konsonan=',num3,'=',nm3)
print('jumlah spassi=',num2,'=',nm2) 
