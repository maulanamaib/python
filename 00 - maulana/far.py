 #bilangann
#n=int(input('masukkan variabel n : '))
#a=int(input('masukkan variabel a : '))
#b=int(input('masukkan variabel b : '))
#for i in range(1, n+1):
#  un=a+(i-1)*b
#  print('u-',i,'=', un)
#  sn=n/2*(a+un)
#print("total =", sn ) 


alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def keyword(text, key) :
    plainText = text
    kunci = key
    panjangKunci = len(kunci)
    x = 0
    cipperText = ''
    for y in range(len(plainText)) :
        indeksP = alfabet.index(plainText[y])
        indeksK = alfabet.index(kunci[x])

        hasil = (indeksP + indeksK) % 26
        cipperText += alfabet[hasil]
        x+=1
        if x == panjangKunci :
            x = 0
    return cipperText

print(keyword('MATEMATIKADISKRET','MAULANAMALIKIBROH'))




