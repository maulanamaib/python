A = []
B = []
R = []
domain = []
Range = []
invers = []
# mencari anggota himpunan A
for i in range(1,101,1):
    A.append(i)
print("Himpunan A",A)
print()

#mencari anggota himpunan B
for j in range(1,21,1):
	if j % 2 == 0 :
		B.append(j)
print("Himpunan B",B)
print()

#mencari relasi himpunan A dan B
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] % B[j] == 0:
	        temp = [A[i],B[j]]
	        R.append(temp)
print("R:",R) 
print()

#untuk mencari Domain
for i in range(len(R)):
	hasil = R[i][0]
	domain.append(hasil)
domain = list(dict.fromkeys(domain))
print("Domain:",sorted(domain))
print()

#mencari Range
for j in range(len(A)):
	for i in range(len(B)):
         if A[j] == B[i]:
            Range.append(A[j])
print("Range:",Range)
print()

#mencari Invers dari R
for i in range(len(R)):
	temp = R[i][0]
	R[i][0] = R[i][1]
	R[i][1] = temp
	invers.append(R[i])
print("Invers R:",invers)
