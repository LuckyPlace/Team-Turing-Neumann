def op_priority(op):
    if op in ['+', '-']:
        return 1
    elif op == '*':
        return 2

def infix_to_postfix(expr, stack, number, postfix):
    for token in expr:
        if(len(token) == 1):
            if token[0] in ['+', '-' ,'*']:
                while stack and op_priority(stack[-1]) >= op_priority(token):
                    postfix.append(stack.pop())
                stack.append(token)
            else:
                number.append(int(token))
        else:
            number.append(int(token))

    while stack:
        postfix.append(stack.pop())

    return postfix

def clear(number, postfix):
    postfix.clear()
    number.clear()




def calc_postfix(postfix, number):
    result = 0

    for token in postfix:
        second = number.pop()
        first = number.pop()
        op = token[0]
        if op == '+':
            result = first + second
        elif op == '-':
            result = first - second
        elif op == '*':
            result = first * second
        number.append(result)
        

    return result


if __name__ == "__main__":

    postfix = []
    stack = []
    number = []
    expr = []

    while True :

        testfunction(number, postfix)
        break

        temp = input()
        temp2 = temp
        if(temp == "1225"):
            print("허허 메리 크리스마스")
            break
        if(temp == '='):
            infix_to_postfix(expr, stack, number, postfix)
            print("{:d}".format(calc_postfix(expr, number)))
            break
        if not temp in ['+', '-' ,'*']:
            assert float(temp)%1 == 0, "Error"
                
        expr.append(temp)


