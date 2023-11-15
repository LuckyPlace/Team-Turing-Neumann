import random
import sys

random.seed(0,2)

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

def clear(expr, postfix, dummy):
    postfix.clear()
    expr.clear()
    dummy.clear()

def testfunction(expr, postfix):

    dummy = []

    #test1
    print("error1", end = "") #error 메시지 출력, error가 발생하였을 때 어디서 오류가 발생하였는지 알아보기 위한 트릭
    clear(expr, postfix, dummy) #expr, postfix, dummy 리스트 초기화
    for i in range(1,10001): #1~10000까지의 수를 더하는 연산을 하여 큰 규모의 더하기 연산에 대하여 테스트 함
        expr.append(str(i))
        if i == 10000:
            break
        expr.append('+')
    
    infix_to_postfix(expr, postfix)
    assert 50005000 == calc_postfix(postfix, dummy), "sum plus error"
    print('\b''\b''\b''\b''\b''\b', end = "") #\b를 호출해서 cursor을 원위치로 돌린다
    
    #test2
    print("error2", end = "") # cursor위치가 되돌려졌고 그 위치에서부터 덮어써진다
    clear(expr, postfix, dummy)
    for i in range(1,10001): #-1~-10000까지의 수를 더하는 연산을 하여 큰 규모의 더하기 연산에 대하여 테스트 함
        expr.append(str(-i))
        if i == 10000:
              break
        expr.append('+')

    infix_to_postfix(expr, postfix)
    assert -50005000 == calc_postfix(postfix, dummy), "sum minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test3
    print("error3", end = "")
    clear(expr, postfix, dummy)
    for i in range(1,10001): #1~10000까지의 수를 빼는 연산을 하여 큰 규모의 빼기 연산에 대하여 테스트 함
        expr.append(str(i))
        if i == 10000:
            break
        expr.append('-')
    
    infix_to_postfix(expr, postfix)
    
    assert -50004998 == calc_postfix(postfix,dummy), "minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")
    
    #test4
    print("error4", end = "")
    clear(expr, postfix, dummy)
    for i in range(1,10001): #-1~-10000까지의 수를 빼는 연산을 하여 큰 규모의 빼기 연산에 대하여 테스트 함
        expr.append(str(-i))
        if i == 10000:
            break
        expr.append('-')
    
    infix_to_postfix(expr, postfix)
    
    assert 50004998 == calc_postfix(postfix,dummy), "minus error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test5
    print("error5", end = "")
    clear(expr, postfix, dummy)
    for i in range(1,3073): #2^3072를 연산하여 큰 규모의 양의 정수 곱하기 연산에 대하여 테스트 함
        expr.append(str(2))
        if i == 3072:
            break
        expr.append('*')

    infix_to_postfix(expr, postfix)
    assert 5809605995369958062859502533304574370686975176362895236661486152287203730997110225737336044533118407251326157754980517443990529594540047121662885672187032401032111639706440498844049850989051627200244765807041812394729680540024104827976584369381522292361208779044769892743225751738076979568811309579125511333093243519553784816306381580161860200247492568448150242515304449577187604136428738580990172551573934146255830366405915000869643732053218566832545291107903722831634138599586406690325959725187447169059540805012310209639011750748760017095360734234945757416272994856013308616958529958304677637019181594088528345061285863898271763457294883546638879554311615446446330199254382340016292057090751175533888161918987295591531536698701292267685465517437915790823154844634780260102891718032495396075041899485513811126977307478969074857043710716150121315922024556759241239013152919710956468406379442914941614357107914462567329693696\
        == calc_postfix(postfix, dummy), "big integer error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test6
    print("error6", end = "")
    clear(expr, postfix, dummy)
    for i in range(1,3073): #(-2)^3072를 연산하여 큰 규모의 음의 정수 곱하기 연산에 대하여 테스트 함
        expr.append(str(-2))
        if i == 3072:
            break
        expr.append('*')
    
    infix_to_postfix(expr, postfix)
    assert 5809605995369958062859502533304574370686975176362895236661486152287203730997110225737336044533118407251326157754980517443990529594540047121662885672187032401032111639706440498844049850989051627200244765807041812394729680540024104827976584369381522292361208779044769892743225751738076979568811309579125511333093243519553784816306381580161860200247492568448150242515304449577187604136428738580990172551573934146255830366405915000869643732053218566832545291107903722831634138599586406690325959725187447169059540805012310209639011750748760017095360734234945757416272994856013308616958529958304677637019181594088528345061285863898271763457294883546638879554311615446446330199254382340016292057090751175533888161918987295591531536698701292267685465517437915790823154844634780260102891718032495396075041899485513811126977307478969074857043710716150121315922024556759241239013152919710956468406379442914941614357107914462567329693696\
        == calc_postfix(postfix, dummy), "big integer2 error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test7
    print("error7", end = "")
    clear(expr, postfix, dummy)

    for i in range(1,401) : #400!을 연산하여 큰 규모의 정수 곱하기 연산에 대하여 테스트 함
        expr.append(str(i))
        if i == 400:
            break
        expr.append('*')

    infix_to_postfix(expr, postfix)

    assert 64034522846623895262347970319503005850702583026002959458684445942802397169186831436278478647463264676294350575035856810848298162883517435228961988646802997937341654150838162426461942352307046244325015114448670890662773914918117331955996440709549671345290477020322434911210797593280795101545372667251627877890009349763765710326350331533965349868386831339352024373788157786791506311858702618270169819740062983025308591298346162272304558339520759611505302236086810433297255194852674432232438669948422404232599805551610635942376961399231917134063858996537970147827206606320217379472010321356624613809077942304597360699567595836096158715129913822286578579549361617654480453222007825818400848436415591229454275384803558374518022675900061399560145595206127211192918105032491008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\
        == calc_postfix(postfix, dummy), "big integer factorial error"
    print('\b''\b''\b''\b''\b''\b', end = "")

    #test8
    print("error8", end = "")
    clear(expr, postfix, dummy)

    for i in range(0,1000): #임의의 정수와 임의의 연산자들의 집합의 연산에 정삭적으로 작동하는지에 대하여 테스트 함
        expr.append(str(random.randint(0,256)))
        d = random.randint(0,256)
        if i == 999:
            continue
        if (d % 3 == 0): 
            expr.append('+')
        elif (d % 3 == 1):
            expr.append('-')
        elif (d % 3 == 2):
            expr.append('*')

    infix_to_postfix(expr, postfix)
    assert 176515113295 == calc_postfix(postfix, dummy), "big calculation error"
    print('\b''\b''\b''\b''\b''\b', end = "")


    print("test complete, No abnormality found")
    
    sys.exit(0)

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
            #testfunction(expr,postfix)     # test가 필요할 경우만 사용
            temp = input()
            if temp in operators and not is_operator:   # 입력이 연산자이고 is_operator가 True가 아닌 경우
                is_right = False        # 비정상적인 입력으로 판정하고 is_right에 False를 대입
            if(is_operator):        # 입력을 받을 때마다 정상적인 입력인지 확인하기 위해 
                is_operator = False # 번갈아가며 False, True변경
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