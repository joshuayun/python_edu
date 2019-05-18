"""
원금 , 연이율(%단위), 이자지급횟수(정수), 거치기간(연단위)
최종원리금
원리금 = 원금 (1+연이율/이자지급횟수)^(이자지급횟수*거치기간)
"""

# 프로그램을 무한 반복 시키기
# 메뉴 구성
# 1. 원리금 계산하기
# 2. 프로그램 종료하기
while True:
    print("----MENU----")
    print("1. 원리금 계산하기")
    print("2. 프로그램 종료하기")
    menu = input("메뉴를 선택하세요: ")
    # 사용자가 선택한 값 1이냐 2이냐에 따라서 하는일을 나누고 싶다.
    # 분기 -> if 구문
    # 1번을 선택했을 때 - 원리금 계산
    # 2번을 선택했을 때 - 프로그램을 종료한다 - exit()

    if menu == '1':
        # 원리금 계산 로직
        # Todo: 함수로 코드 단순화 하기, 모듈화 하기
        while True:
            balance = input("원금을 입력하세요.(원): ")
            try:
                balance = int(balance)
                break
            except:
                print("원금을 다시 입력하세요.")

        while True:
            interest = input("연이율을 입력하세요.(%): ")
            try:
                interest = float(interest)
                break
            except:
                print("연이율을 다시 입력하세요.")
        while True:
            number_of_count = input("연 지급횟수를 입력하세요.: ")
            try:
                number_of_count = int(number_of_count)
                break
            except:
                print("연 지급횟수 다시 입력하세요.")
        while True:
            number_of_year = input("거치기간을 입력하세요.(연단위):  ")
            try:
                number_of_year = int(number_of_year)
                break
            except:
                print("거치기간을 다시 입력하세요.")
        #원리금 = 원금(1 + 연이율 / 이자지급횟수) ^ (이자지급횟수 * 거치기간)
        final_balance = balance * (1 + ((interest/100) / number_of_count)) ** (number_of_count * number_of_year)
        print("최종원리금은 %d원 입니다." % (final_balance))


    elif menu == '2':
        print("프로그램을 종료합니다.")
        break # exit()
    else:
        print("없는 메뉴입니다.")