def op_priority(op):
    if op in ['+', '-']:
        return 1
    elif op == '*':
        return 2

def infix_to_postfix(expr, stack, number, postfix):
    stack2 = []
    temp = []
    for token in expr:
        if(len(token) == 1):
            if token[0] in ['+', '-' ,'*']:
                while stack and op_priority(stack[-1]) >= op_priority(token):
                    postfix.append(stack.pop())
                    temp.append(stack2.pop())
                stack.append(token)
            else:
                stack2.append(int(token))
        else:
            stack2.append(int(token))

    while stack:
        postfix.append(stack.pop())

    while stack2:
        temp.append(stack2.pop())

    while temp:
        number.append(temp.pop())

    return postfix

def calc_postfix(postfix, number):
    result = 0

    for token in postfix:
        first = number.pop()
        second = number.pop()
        op = token[0]
        if op == '+':
            result = first + second
        elif op == '-':
            print("error")
            result = first - second
        elif op == '*':
            result = first * second
        number.insert(0, result)
        
    return result


if __name__ == "__main__":

    postfix = []
    stack = []
    number = []
    expr = []
    bo = 0

    while True:

        #testfunction(number, postfix)
        #break

        temp = input()

        if bo :
               if not temp in ['+', '-' ,'*']: 
                    if temp[0] == '-':
                        temp.replace('-','')
                        bo = 0
                    else:
                        temp = "-" + temp
                        bo = 0
                        
        if temp == '-':
            expr.append('+')
            bo = 1
            continue      
        if(temp == "1225"):
            print("허허 메리 크리스마스")
            break
        if(temp == '='):
            infix_to_postfix(expr, stack, number, postfix)
            if not len(number) - 1 ==  len(postfix):
                print("Error")
            print("{:d}".format(calc_postfix(postfix, number)))
            break
        if not temp in ['+', '-' ,'*']:
            assert float(temp)%1 == 0, "Error"
                
        expr.append(temp)


def clear(number, postfix):
    postfix.clear()
    number.clear()

def testfunction(number, postfix):

    print("error1", end = "") #error 메시지 출력
    clear(number, postfix) #number, postfix 리스트 초기화
    for i in range(1,10001):
        number.append(i)
    
    for i in range(1,10000):
        postfix.append('+')
    assert 50005000 == calc_postfix(postfix, number), "sum plus error"
    print('\b''\b''\b''\b''\b''\b', end = "") #출력
    
    print("error2", end = "")
    clear(number, postfix)
    for i in range(1,10001):
        number.append(-i)
    
    for i in range(1,10000):
        postfix.append('+')

    assert -50005000 == calc_postfix(postfix, number), "sum minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    print("error3", end = "")
    clear(number, postfix)
    for i in range(1,10001):
        number.append(1)
    
    for i in range(1,10000):
       postfix.append('-')

    assert 0 == calc_postfix(postfix,number), "minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")
    
    print("error4", end = "")
    clear(number, postfix)
    for i in range(1,3073):
        number.append(2)
    
    for i in range(1,3072):
        postfix.append('*')

    assert 5809605995369958062859502533304574370686975176362895236661486152287203730997110225737336044533118407251326157754980517443990529594540047121662885672187032401032111639706440498844049850989051627200244765807041812394729680540024104827976584369381522292361208779044769892743225751738076979568811309579125511333093243519553784816306381580161860200247492568448150242515304449577187604136428738580990172551573934146255830366405915000869643732053218566832545291107903722831634138599586406690325959725187447169059540805012310209639011750748760017095360734234945757416272994856013308616958529958304677637019181594088528345061285863898271763457294883546638879554311615446446330199254382340016292057090751175533888161918987295591531536698701292267685465517437915790823154844634780260102891718032495396075041899485513811126977307478969074857043710716150121315922024556759241239013152919710956468406379442914941614357107914462567329693696\
        == calc_postfix(postfix, number), "big integer error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    print("error5", end = "")
    clear(number, postfix)
    for i in range(1,3073):
        number.append(-2)
    
    for i in range(1,3072):
        postfix.append('*')

    assert 5809605995369958062859502533304574370686975176362895236661486152287203730997110225737336044533118407251326157754980517443990529594540047121662885672187032401032111639706440498844049850989051627200244765807041812394729680540024104827976584369381522292361208779044769892743225751738076979568811309579125511333093243519553784816306381580161860200247492568448150242515304449577187604136428738580990172551573934146255830366405915000869643732053218566832545291107903722831634138599586406690325959725187447169059540805012310209639011750748760017095360734234945757416272994856013308616958529958304677637019181594088528345061285863898271763457294883546638879554311615446446330199254382340016292057090751175533888161918987295591531536698701292267685465517437915790823154844634780260102891718032495396075041899485513811126977307478969074857043710716150121315922024556759241239013152919710956468406379442914941614357107914462567329693696\
        == calc_postfix(postfix, number), "big integer2 error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    print("error6", end = "")
    clear(number, postfix)
    for i in range(1,401):
        number.append(i)
    
    for i in range(1,400):
        postfix.append('*')

    assert 64034522846623895262347970319503005850702583026002959458684445942802397169186831436278478647463264676294350575035856810848298162883517435228961988646802997937341654150838162426461942352307046244325015114448670890662773914918117331955996440709549671345290477020322434911210797593280795101545372667251627877890009349763765710326350331533965349868386831339352024373788157786791506311858702618270169819740062983025308591298346162272304558339520759611505302236086810433297255194852674432232438669948422404232599805551610635942376961399231917134063858996537970147827206606320217379472010321356624613809077942304597360699567595836096158715129913822286578579549361617654480453222007825818400848436415591229454275384803558374518022675900061399560145595206127211192918105032491008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\
        == calc_postfix(postfix, number), "big integer factorial error"
    print('\b''\b''\b''\b''\b''\b', end = "")




    print("test complete, No abnormality found")