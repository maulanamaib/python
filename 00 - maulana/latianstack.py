def stack():
    s=[]
    return (s)
def push(s,data):
    s.append(data)
def pop(s):
    data=s.pop()
    return (data)
def peek(s):
    return(s[len(s)-1])
def isEmpty(s):
    return (s==[])
def size(s):
    return (len(s))
    
def evaluatePost(postStr):
    operandStack=st.stack()
    operator="+-/*"
    for i in postStr:
        if i not in operator:
            st.push(operandStack,i)
        else:
            oprnd2=st.pop(operandStack)
            oprnd1=st.pop(operandStack)
            if i =="+":
                result=int(oprnd1)+int(oprnd2)
            elif i=="-":
                result=int(oprnd1)-int(oprnd2)
            elif i=="*":
                result=int(oprnd1)*int(oprnd2)
            else:
                result=int(oprnd1)/int(oprnd2)
            st.push(operandStack,result)
    return(st.pop(operandStack))
    
def checkParantheses(strMat):
    data=st.stack()
    for i in strMat:
        if i=="(" or i=='[' or i=='{':
                st.push(data,i)
        elif i==")" or i=="]" or i=='}':
            if st.isEmpty(data):
                return "Jumlah kurung tutup lebih banyak"
            else:
                if st.peek(data)=="(" and i==")":
                    st.pop(data)
                elif st.peek(data)=="[" and i=="]":
                    st.pop(data)
                elif st.peek(data)=="{" and i=="}":
                    st.pop(data)
                else:
                    print("Kurung buka dan kurung tutup tidak cocok")
    if st.isEmpty(data):
        return True

                # Aux operations
        def isOperand(c):
            return c >= '0' and c <= '9'

        operators = "+-*/^"

        def isOperator(c):
            return c in operators

        def getPrecedence(c):
            result = 0

            for char in operators:
                result += 1

                if char == c:
                    if c in '-/':
                        result -= 1
                    break

            return result

        # ~~~~~~~~~~~~
        # infix to postfix
        def toPostfix(expression):
            result = ""

            stack = Stack(15)

            for char in expression:
                if isOperand(char):
                    result += char
                elif isOperator(char):
                    while True:
                        topChar = stack.topChar()

                        if stack.isEmpty() or topChar == '(':
                            stack.push(char)
                            break
                        else:
                            pC = getPrecedence(char)
                            pTC = getPrecedence(topChar)

                            if pC > pTC:
                                stack.push(char)
                                break
                            else:
                                result += stack.pop()

                elif char == '(':
                    stack.push(char)
                elif char == ')':
                    cpop = stack.pop()

                    while cpop != '(':
                        result += cpop
                        cpop = stack.pop()

            while not stack.isEmpty():
                cpop = stack.pop()
                result += cpop
            return result
        return (toPostfix(expression))

        # ~~~~~~~~~~~~
        # test
   
    else:
        return 'Jumlah kurung buka lebih banyak'
print(checkParantheses)