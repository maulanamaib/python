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
    div=0
    div2=""
    while num!=0:
      if num%2==1:
        div=(num-1)/2
        push(temp,"1")
        print("%i div 2 = %i sisa 1: push(stack,1)\n"%(num,div))
        num=div
        for i in temp[::-1]:
          print("| %s |"%i)
        print("-----")
      elif num%2==0:
        div=num/2
        push(temp,"0")
        print("%i div 2 =%i sisa 0: push(stack,0)\n"%(num,div))
        num=div
        for i in temp[::-1]:
          print("| %s |"%i)
        print("-----")
    num=num-1
   
    
    for i in temp[::-1]:
      div2=div2+pop(temp)
    return div2

print("binner 25 =",convertBinary(19))
      