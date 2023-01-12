#def print_faktor(x):
#    listfaktor=[]
#    print("Faktor dari", x, "adalah:")
#    for i in range(1, x+1):
#        if x % i == 0:
#            listfaktor.append(i)
#    return listfaktor        
#        
#num = int(input("Masukkan bilangan: "))
#print(print_faktor(num))
# n=int(input("Masukkan Variabel n= "))
# rum=0
# y=0
# for i in range(n):
#     rum=rum+i
#     if rum>=10 :
#        wx=1
#     else :
#        wx=0
#     yah=1/n*wx*rum
#     print("1/n*W(Xi)*Sigma:",i,"=", rum)
# print("Sigma = " , yah)

# n=int(input("masukan angka :"))
# hasil=[]
# for i in range(n):
#     if i%2==0:
#         hasil.append(i)
# print(hasil)

list1= [1,2,3]
list2= list1
list1.append(list2)
print(list1)