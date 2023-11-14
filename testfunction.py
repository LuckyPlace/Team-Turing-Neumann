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
        postfix.append('+')

    assert 50005000 == calc_postfix(), "sum plus error"
    print('\b''\b''\b''\b''\b''\b', end = "")
    
    print("error2", end = "")
    clear()
    for i in range(1,10001):
        number.append(-i)
    
    for i in range(1,10000):
        postfix.append('+')

    assert -50005000 == calc_postfix(), "sum minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    print("error3", end = "")
    clear()
    for i in range(1,10001):
        number.append(1)
    
    for i in range(1,10000):
       postfix.append('-')

    assert 0 == calc_postfix(), "minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")
    
    print("error4", end = "")
    clear()
    for i in range(1,3073):
        number.append(2)
    
    for i in range(1,3072):
        postfix.append('*')

    assert 5809605995369958062859502533304574370686975176362895236661486152287203730997110225737336044533118407251326157754980517443990529594540047121662885672187032401032111639706440498844049850989051627200244765807041812394729680540024104827976584369381522292361208779044769892743225751738076979568811309579125511333093243519553784816306381580161860200247492568448150242515304449577187604136428738580990172551573934146255830366405915000869643732053218566832545291107903722831634138599586406690325959725187447169059540805012310209639011750748760017095360734234945757416272994856013308616958529958304677637019181594088528345061285863898271763457294883546638879554311615446446330199254382340016292057090751175533888161918987295591531536698701292267685465517437915790823154844634780260102891718032495396075041899485513811126977307478969074857043710716150121315922024556759241239013152919710956468406379442914941614357107914462567329693696\
        == calc_postfix(), "big integer error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    print("error5", end = "")
    clear()
    for i in range(1,3073):
        number.append(-2)
    
    for i in range(1,3072):
        postfix.append('*')

    assert 5809605995369958062859502533304574370686975176362895236661486152287203730997110225737336044533118407251326157754980517443990529594540047121662885672187032401032111639706440498844049850989051627200244765807041812394729680540024104827976584369381522292361208779044769892743225751738076979568811309579125511333093243519553784816306381580161860200247492568448150242515304449577187604136428738580990172551573934146255830366405915000869643732053218566832545291107903722831634138599586406690325959725187447169059540805012310209639011750748760017095360734234945757416272994856013308616958529958304677637019181594088528345061285863898271763457294883546638879554311615446446330199254382340016292057090751175533888161918987295591531536698701292267685465517437915790823154844634780260102891718032495396075041899485513811126977307478969074857043710716150121315922024556759241239013152919710956468406379442914941614357107914462567329693696\
        == calc_postfix(), "big integer2 error"
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


