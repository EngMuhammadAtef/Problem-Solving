def convertToPostfix(equ):
    stack = []
    pstfix = []

    # Converting to Postfix
    for i in range(len(equ)):
        if equ[i] in '+-': # + -
            if len(stack)==0:
                stack.append(equ[i])
            else:
                if stack[-1] in '+-':
                    pstfix.append(stack[-1])
                    stack.pop()
                    stack.append(equ[i])
                elif stack[-1] in '*/':
                    while len(stack)!=0 and stack[-1] not in '([{':
                        pstfix.append(stack[-1])
                        stack.pop()
                    stack.append(equ[i])
                else:
                    stack.append(equ[i])   
        
        elif equ[i] in '*/': # * /
            if len(stack)==0:
                stack.append(equ[i])
            else:
                if stack[-1] in '+-':
                    stack.append(equ[i])
                elif stack[-1] in '*/':
                    pstfix.append(stack[-1])
                    stack.pop()
                    stack.append(equ[i])
                else:
                    stack.append(equ[i])

        elif equ[i] in ')]}([{': # {[()]}
            if equ[i] in '([{':
                stack.append(equ[i])
            else:
                while stack[-1] not in '([{':
                    pstfix.append(stack[-1])
                    stack.pop()
                stack.pop() # to delete ( [ {

        else: # Number
            pstfix.append(equ[i])

    # Pop stack's Elements
    while len(stack)!=0:
        pstfix.append(stack[-1])
        stack.pop()

    return pstfix

def EvalPostfixExp(exp):
    stack = []
    result = 0

    for i in range(len(exp)): #  1 2 + 3 - 4 * 5 +
        if exp[i] == "+":
            secO = stack.pop()
            frsO = stack.pop()
            result = int(frsO) + int(secO)
            stack.append(result)
        elif exp[i] == "-":
            secO = stack.pop()
            frsO = stack.pop()
            result = int(frsO) - int(secO)
            stack.append(result)
        elif exp[i] == "*":
            secO = stack.pop()
            frsO = stack.pop()
            result = int(frsO) * int(secO)
            stack.append(result)
        elif exp[i] == "/":
            secO = stack.pop()
            frsO = stack.pop()
            if int(secO) != 0:
                result = int(frsO) / int(secO)
                stack.append(result)
            else:
                return "ZeroDivisionError: division by zero"
        else: # Number
            stack.append(exp[i])
    return result

# Test Cases
# 5 + 4 * 3 - ( 5 / 1 + 5 )  = 7
# ( ( 1 + 2 ) - 3 ) * 4 + 5  = 5

equ = list(input().split())

# Print Infix format
print('Infix: ', *equ)

pstfix = convertToPostfix(equ)
# Print Postfix format
print('Postfix: ', *pstfix)
# Print Evalaution of Postfix Expression
print('Evalaution: ', EvalPostfixExp(pstfix))