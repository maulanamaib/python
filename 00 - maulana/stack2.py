def stack():
 s=[]
 return (s)
def push(s,data):
 s.append(data)
def pop(s):
 data=s.pop()
 return(data)
def peek(s):
 return(s[len(s)-1])
def isEmpty(s):
 return (s==[])
def size(s):
 return(len(s))

def convertBinary(num):
    temp=stack()
    divNum=num
    while divNum>0:
      push(temp,divNum%2)
      divNum=divNum//2
    tempStr=''
    for i in range(size(temp)):
        tempStr=tempStr+str(pop(temp))
    return tempStr
    
print(convertBinary(25))