#2.2
#def sumstringDigit(x):
#  k=len(x)-1
#  if k==0:
#    return int(x[0])
#  else :
#    return int(x[k])+sumstringDigit(x[:k])
#
#strNum="4364725"
#print("Total penjumlahan dari digit ",strNum," adalah ",sumstringDigit(strNum))

#2.1
def maxNumber(data) :
    x = len(data)
    if x == 1 :
        maxs = data[a-1]
        return maxs
    if maxNumber(data[1:]) > data[0] :
        return maxNumber(data[1:])
    else :
        return data[0]

data = [9, 1, 3, 5, 7, 7, 5]
print("Bilangan maksimal dari ", data, "adalah ", maxNumber(data))

#2.2
def sumStringDigit(angka) :
    a = len(angka)
    if a-1 == 0 :
        return int(angka)
    else :
        return int(angka[0]) + sumStringDigit((angka[1:]))

strNum = '456'
print("Total penjumlahan dari digit ", strNum, "adalah", sumStringDigit(strNum) )