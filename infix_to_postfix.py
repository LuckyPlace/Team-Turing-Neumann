def infix_to_postfix(expr):
    postfix = []
    stack = []

    #음수 구현 아이디어 : 숫자가 아니면서 한 글자면 연산자로 판정, 그 외에는 피연산자(숫자)로 판정
    for token in expr:
        if token[0] in ['+', '-' ,'*']:
            #stack의 top()에 있는 연산자의 우선순위가 token의 연산자보다 크거나 같다면
            #postfix에 stack의 top()을 append하고 stack을 pop()한다. 그리고 stack에 token을 append한다.
        else:
            postfix.append(token)

    while stack:
        postfix.append(stack.pop())

    return postfix