import sys

def op_priority(op):       # 연산자의 우선순위를 결정하는 함수
    if op in ['+', '-']:
        return 1
    elif op == '*':        # '*' 연산자의 우선순위가 더 높으므로 1보다 더 큰 2를 리턴
        return 2

def infix_to_postfix(expr, postfix): # infix를 postfix로 바꾸는 함수
    stack = []          # stack으로 활용하기 위한 list 선언
    for token in expr:
        if len(token) == 1 and token[0] in ['+', '-', '*']: #길이가 1인 경우 양의 정수이거나 연산자
            while stack and op_priority(stack[-1]) >= op_priority(token):
                postfix.append(stack.pop()) # 스택의 맨위에 있는 연산자가 더 크거나 같은 연산자일 때까지 stack에서 pop()한 것을 postfix list에 저장하고
            stack.append(token) # stack에 현재 값을 넣어준다.
        else:   #나머지의 경우
            postfix.append(token)     # 음의 정수인 경우 int형으로 바꿔 number list에 저장한다.

    while stack:
        postfix.append(stack.pop())     # stack에 남아있는 연산자들을 postfix list에 추가한다.

def calc_postfix(postfix, tmp):     # infix_to_postfix함수로부터 리턴된 postfix를 계산하는 함수
    result = 0
    for token in postfix:
        if len(token) == 1 and token[0] in ['+', '-', '*']:
            second = tmp.pop()
            first = tmp.pop()
            op = token[0]
            if op == '+':       # +인 경우 계산
                result = first + second
            elif op == '-':     # -인 경우 계산
                result = first - second
            elif op == '*':     # *인 경우 계산
                result = first * second
            tmp.append(result)
        else:
            tmp.append(int(token))
    return result

def print_error():
    print("ERROR!")
    sys.exit()

if __name__ == "__main__":
    expr = []           # 식을 저장하기 위해 list 선언
    postfix = []        # infix를 postfix로 바꾼 표현을 저장하는 list 선언
    tmp = []            # calc_postfix()함수에서 사용할 stack 선언
    ans = 0             # 답 임시 저장 변수
    is_operator = False     # 333++같이 연속으로 숫자가 나오는 경우를 막기 위한 변수
    is_right = True
    operators = ['+', '-', '*']
    while True :
        try:
            temp = input()
            if temp in operators and not is_operator:
                is_right = False
            if(is_operator):
                is_operator = False
            else:
                is_operator = True
            if(temp == "1225"):     # 이스터에그 : 크리스마스인 1225를 입력하면 발생
                print("허허 메리 크리스마스")
                break
            if(temp == '='):        # '='가 입력된 경우 지금까지 입력된 expr을 함수에 전달해 계산
                if not expr:       # 아무것도 입력하지 않고 '='를 입력한 경우
                    print_error()
                if not is_right:
                    print_error()
                infix_to_postfix(expr, postfix)
                ans = calc_postfix(postfix, tmp)
                if len(tmp) > 1:        # tmp list가 1보다 클 경우 숫자가 비정상적으로 많다.
                    print_error()
                print(ans)
                break
            expr.append(temp)
        except Exception:
            print_error()