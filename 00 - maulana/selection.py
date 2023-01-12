data=[9,4,5,2,3,1]
for start in range (len(data)-1):
    flag=start
    for i in range(start+1,len(data)):
        print(flag,i)
        if data[flag]>data[i]:
            flag=i
    data[start], data[flag] = data[flag], data[start]
    print(data)