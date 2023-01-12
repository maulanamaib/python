def bentukmatriks(x) :
    for i in range(len(x)):
        print("|", end='')
        for y in range(len(x[0])):
            print("%4s"%str(x[i][y]), end='')
        print(" |")
    print(" ")

def bagianmatriks3D(x,y) :
    r = []
    for i in range(len(x)):
        hasil2 = []
        for j in range(len(y)):
            if x[i] % y[j] == 0 :
                hasil2.append(1)
                #hasil2.extend((x[i],y[j]))
            #elif x[i] % y[j] == 0 :
              #  r.append([x[i],y[j]])
            else :
                #pass
                hasil2.append(0)
        r.append(hasil2)
    return sorted(r) 

def invers(x) :
    for i in range(len(x[0])):
        print("|", end='')
        for y in range(len(x)):
            print("%4s"%str(x[y][i]), end='')
        print(" |")
    print(" ")

list1 = [2,3,4,5]
list2 = [3,6,7,10]
matrix = bagianmatriks3D(list1,list2)
print(matrix)
bentukmatriks(matrix)
invers(matrix)