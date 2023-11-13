postfix = []
stack = []
number = []
expr = []

def op_priority(op):
    if op in ['+', '-']:
        return 1
    elif op == '*':
        return 2

def infix_to_postfix():
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

def calculator():
    expr = infix_to_postfix()
    return calc_postfix()

def clear():
    postfix.clear()
    stack.clear()
    number.clear()
    expr.clear()

def testfunction():

    print("error1", end = "")
    clear()
    for i in range(1,10001):
        number.append(i)
    
    for i in range(1,10000):
        expr.append('+')

    assert 50005000 == calculator(), "sum plus error"
    print('\b''\b''\b''\b''\b''\b', end = "")
    
    print("error2", end = "")
    clear()
    for i in range(1,10001):
        number.append(-i)
    
    for i in range(1,10000):
        expr.append('+')

    assert -50005000 == calculator(), "sum minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    print("error3", end = "")
    clear()
    for i in range(1,10001):
        number.append(1)
    
    for i in range(1,10000):
        expr.append('-')

    assert 0 == calculator(), "minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")
    
    print("error4", end = "")
    clear()
    for i in range(1,3025):
        number.append(2)
    
    for i in range(1,3024):
        expr.append('*')

    assert 20639866688192249678690979427047744716670419422978338405490767656712605070613300830961151335902735607601692030339466006139980896685912793208440823179426475068368459772139688719662053454545441962864930352619700970232691192549708975533834320861293755528582525396944795278184961346348121152405537193811559544560528122472766855879578363826574119600278907314987542926997237378746730499786212713008347110671443879490481628971586456347856297569099192539115056245819004213727631262285862613802315336376080691028745451394187818329012215737168247703065165176763236436188268622714806030476205940112438517662309257595469092710023367459009590744249233592976505063469657896200879783774178059516715294055766886940027007433396687814278648206918025537489162479394046257364519031954709690026927019765539112214281096766958661032472041467681013226556685362979770990378092763807981815343641872998542497684604695404128952469438857216  \
        == calculator(), "big integer error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    print("test complete, No abnormality found")


def calc_postfix():
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

    while True :

        testfunction()
        break

        temp = input()
        temp2 = temp
        if(temp == "1225"):
            print("허허 메리 크리스마스")
            break
        if(temp == '='):
            infix_to_postfix()
            print("{:d}".format(calc_postfix()))
            break
        expr.append(temp)


