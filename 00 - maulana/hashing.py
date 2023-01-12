import random

def generate_random(jumlah,min,max):
    data=[]
    for i in range (jumlah):
        data.append(random.randint(min,max))
    return data

def remainderFuction(data,num):
    return (data%num)

def createHashtable (num):
    temp=[]
    for i in range(num):
        temp.append(['none'])
    return(temp)

def putData(data,table):
    for i in range(len(data)):
        ind=remainderFuction(data[i],len(table))
        if table[ind][0]=='none':
            table[ind][0]=data[i]
        else:
            t=table[ind]
            t.append(data[i])
    return(table)

def searchHash(data,table):
    hashVal=remainderFuction(data,table)
    if table[hashVal]!='none':
        for i in range(len(table[hashVal])):
            if data==table[hashVal][i]:
                return (hashVal,i,True)
    else:
        return False

data = generate_random(500,0,10000)
#data =[2,3,4,5,6,7,8,9,1,21,34,56,76,45,32]
print(data)
numOfSlot=500
HashTable = createHashtable(numOfSlot)
HashTable = putData(data,HashTable)
findData= 6754
found = searchHash(findData,HashTable)
if not found:
    print('{} Is Not In The Hash Table'.format(findData))
else:
    print('{} Is In Slot {} Index : {}'.format(findData,found[0],found[1]))
    print('Data In Slot [{}] : {}'.format(found[0],HashTable[found[0]]))