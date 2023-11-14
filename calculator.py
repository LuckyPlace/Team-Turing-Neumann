def op_priority(op):       # 연산자의 우선순위를 결정하는 함수
    if op in ['+', '-']:
        return 1
    elif op == '*':        # '*' 연산자의 우선순위가 더 높으므로 1보다 더 큰 2를 리턴
        return 2

def infix_to_postfix(expr, stack, number, postfix): # infix를 postfix로 바꾸는 함수
    for token in expr:
        if(len(token) == 1): #길이가 1인 경우 양의 정수이거나 연산자
            if token[0] in ['+', '-' ,'*']:  # 연산자인 경우 연산자의 우선순위에 따라
                while stack and op_priority(stack[-1]) >= op_priority(token):
                    postfix.append(stack.pop()) # 스택의 맨위에 있는 연산자가 더 크거나 같은 연산자일 때까지 stack에서 pop()한 것을 postfix list에 저장하고
                stack.append(token) # stack에 현재 값을 넣어준다.
            else:
                number.append(int(token))   # 양의 정수인 경우 int형으로 바꿔 number list에 저장한다.
        else:
            number.append(int(token))     # 음의 정수인 경우 int형으로 바꿔 number list에 저장한다.

    while stack:
        postfix.append(stack.pop())     # stack에 남아있는 연산자들을 postfix list에 추가한다.



def calc_postfix(postfix, number):     # infix_to_postfix함수로부터 리턴된 postfix를 계산하는 함수
    result = 0

    for token in postfix:
        second = number.pop()
        first = number.pop()
        op = token[0]
        if op == '+':       # +인 경우 계산
            result = first + second
        elif op == '-':     # -인 경우 계산
            result = first - second
        elif op == '*':     # *인 경우 계산
            result = first * second
        number.append(result)
        
    return result


if __name__ == "__main__":
    expr = []           # 식을 저장하기 위해 list 선언
    postfix = []        # infix를 postfix로 바꾼 표현을 저장하는 list 선언
    stack = []          # stack으로 활용하기 위한 list 선언
    number = []         # 정수만 따로 int형으로 저장하기 위해 list 선언
    while True :
        temp = input()
        if(temp == "1225"):     # 이스터에그 : 크리스마스인 1225를 입력하면 발생
            print("허허 메리 크리스마스")
            break
        if(temp == '='):        # '='가 입력된 경우 지금까지 입력된 expr을 함수에 전달해 계산
            infix_to_postfix(expr, stack, number, postfix)
            print("{:d}".format(calc_postfix(postfix, number)))
            break
        expr.append(temp)