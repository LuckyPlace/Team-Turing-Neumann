def calc_postfix(expr):
    # 후위 표현식을 계산하는 함수
    stack = []  # 계산에 사용할 스택

    for token in expr:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # 토큰이 숫자 또는 음수 값인 경우
            stack.append(float(token))
        elif token in "+-*/":
            # 토큰이 연산자인 경우
            second = stack.pop()
            first = stack.pop()
            if token == '+':
                result = first + second
            elif token == '-':
                result = first - second
            elif token == '*':
                result = first * second
            elif token == '/':
                result = first / second
            stack.append(result)

    return stack[0]

def calculate(expr):
    try:
        postfix_expr = infix_to_postfix(expr)
        result = calc_postfix(postfix_expr)
        return result
    except:
        return "error"

user_input = ""  # 사용자 입력을 저장하는 문자열

while True:
    token = input()  # 사용자로부터 입력을 받음
    if token == '=':
        # 사용자가 '='를 입력하면 계산을 수행하고 결과를 출력
        result = calculate(user_input)
        print(result)
        user_input = ""  # 사용자 입력 초기화
    elif token == 'q':
        # 사용자가 'q'를 입력하면 프로그램 종료
        break
    elif any(c.isalpha() for c in token) or (token.count('.') > 1):
        # 입력이 올바르지 않은 경우 (알파벳 포함 또는 소수점이 여러 개인 경우)
        print("error")
    else:
        user_input += token  # 사용자 입력에 토큰 추가
