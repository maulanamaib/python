def bubleSortModif(x):
    n=len(x)
    i=0
    count=1
    while i < n :
        i = 0
        print("iterasi ke-{} jumlah iterasi - {}".format(count,n-1))
        count += 1
        for j in range(n-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
            else :
                i += 1
            print("{} = {}".format(j+1,x))
        n -= 1
    return x

data=[10,2,5,8,1,20,2,2,4]
print("Data yang diurutkan : ",data)
print("Hasil : ",bubleSortModif(data))