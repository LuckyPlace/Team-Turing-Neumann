import random
import sys

random.seed(0,2)

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