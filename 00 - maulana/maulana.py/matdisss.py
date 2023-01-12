import math
def fungsi(x,y):
    for i in range (-6,x+4):
        #hasil=(i*i)-(2*i)+1
        #hasil2=(hasil*hasil)-(2*hasil)+1
        #
        #hasil= i+4
        #hasil2=hasil+4
        #
        hasil=i*i*i
        hasil2=hasil*hasil*hasil
        #
        #hasil=(i*i*i) - (3*(i*i)) + (3*i)-1 
        #hasil2=(hasil*hasil*hasil) - (3*(hasil*hasil)) + (3*hasil) - 1

        #tampilan
        print(f'Y={i} dan x = {hasil}')
        print(f'Hasil x jika Y = {hasil} = {hasil2}\n')


#program
x = int(input("masukkan x:"))
y = x
fungsi(x,y)
