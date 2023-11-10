def infix_to_postfix(expr):
    postfix = []
    stack = []

    #음수 구현 아이디어 : 숫자가 아니면서 한 글자면 연산자로 판정, 그 외에는 피연산자(숫자)로 판정
    for token in expr:
        if token[0] in ['+', '-' ,'*']:
            #op_priority(): 연산자들의 우선순위 반환하는 함수
            while stack and op_priority(stack[-1]) >= op_priority(token):
                postfix.append(stack.pop())
            stack.append(token)
        else:
            postfix.append(token)

    while stack:
        postfix.append(stack.pop())

    return postfix