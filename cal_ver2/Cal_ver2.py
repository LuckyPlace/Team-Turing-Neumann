postfix = []
stack = []
number = []

def op_priority(op):
    if op in ['+', '-']:
        return 1
    elif op == '*':
        return 2

def infix_to_postfix(expr):

#숫자가 아니면서 한 글자면 연산자로 판정, 그 외에는 피연산자(숫자)로 판정  # 미구현
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


def calc_postfix(expr):
    result = 0
    stack = []

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
        stack.append(result)
        

    return result


if __name__ == "__main__":

    expr = []
    try:
        while True :
            temp = input()
            temp2 = temp
            if(temp == "1225"):
                print("허허 메리 크리스마스")
                break
            if(temp == '='):
                expr = infix_to_postfix(expr)
                print("{:d}".format(calc_postfix(expr)))
                break
            expr.append(temp)
    except:
        print("Error!")