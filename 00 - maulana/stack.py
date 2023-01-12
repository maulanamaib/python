#def stack():
# s=[]
# return (s)
#def push(s,data):
# s.append(data)
#def pop(s):
# data=s.pop()
# return(data)
#def peek(s):
# return(s[len(s)-1])
#def isEmpty(s):
# return (s==[])
#def size(s):
# return(len(s))

#def reverse(word):
#    data=[]
#    for i in range(len(word)):
#        data.append(word[i])
#    stack =''
#    for i in range(len(data)):
#        stack+= data.pop()
#    return stack
#
#print("hasil =",reverse(input("masukkan data =")))


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


#def checkParentheses(strMat):
#    data= std.stack()
#    for ch in strMat:
#        if ch=='(':
#             std.push(data,ch)
#        elif ch==')':
#            if  std.isEmpty(data):
#                return 'kelebihan kurung tutup'
#            else:
#                std.pop(data)
#    if  std.isEmpty(data):
#        return True
#
#    else:
#        return 'Kelebihan kurung buka'
#checkParentheses('5 x (4 + 5) / (3 + 2) x (10 - 8))')
def par(strMat):
  kurung = "()"
  data = stack()
  match = False
  for i in strMat:
    if i in kurung:
      if i == kurung[0]:
        push(data,i)      
      else:
       if size(data) != 0:
          pop(data)
          return "pas"         
       else:
          return "kelebihan kurung tutup"
  if size(data) != 0:
    return "kelebihan kurung buka" 

