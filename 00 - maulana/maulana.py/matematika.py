#1
def bagianmatriks3D(x,y) :
    r = [[1,5],[4,5],[1,4],[4,6],[3,7],[7,6]]
    hasil1 = []
    for i in x:
        hasil2 = []
        for j in y:
            if [i,j] in r :
                hasil2.append(1)
            else :
                hasil2.append(0)
        hasil1.append(hasil2)
    return hasil1 
def bentukmatriks(x) :
    for i in range(len(x)):
        print("|", end='')
        for y in range(len(x[0])):
            print("%4s"%str(x[i][y]), end='')
        print(" |")
    print(" ")
def invers(x) :
    for i in range(len(x[0])):
        print("|", end='')
        for y in range(len(x)):
            print("%4s"%str(x[y][i]), end='')
        print(" |")
    print(" ")

list1 = [1,2,3,4,5,6,7]
list2 = [4,5,6,7,8,9]
matrix = bagianmatriks3D(list1,list2)
bentukmatriks(matrix)
invers(matrix)





