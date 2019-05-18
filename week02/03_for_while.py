"""
반복문
for : 정해진 횟수 동안
while : ~ 조건이 유지되는 동안
"""

#1 ~ 10 까지 출력을 하고 싶다.

number = 1
# 중복되는 부분을 반복문 안에서 처리하고
# 바뀌어야 하는 부분이 무엇인지 고민한다.

"""
while number <= 10:
    print(number)
    number = number + 1
    #number += 1
"""

"""
while [조건문]:
    [실행구문]
"""

"""
while True:
    # 데이터를 입력받는데 언제 끝낼지 모를 때
    # 프로그램 전체를 반복할 때
    # 데이터 입력이 올바를 경우만 종료하고 싶을 때
"""
while True:
    weight = input("체중을 입력하세요.: ")
    try:
        weight = float(weight)
        if weight > 0:
            break
    except:
        print("입력값이 올바르지 않습니다.")

while True:
    height = input("신장을 입력하세요.: ")
    try:
        height = float(height)
        if height > 0:
            break
    except:
        print("입력값이 올바르지 않습니다.")

