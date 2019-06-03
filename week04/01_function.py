"""
함수 : 만들고 쓸줄 알아야 합니다.
input()
print()
random.randint(1,2)
datetime.now()
int()
str()

함수는 한꺼번에 여러 종류의 일을 연속으로 처리하고 싶을 때
묶어서 만들어 두는 기능

실생활에서 함수의 예 : 자판기
입력(매개변수) : 돈, 음료 선택
처리 : 잔돈 계산, 음료 찾기
출력(반환값) : 잔돈, 음료캔
"""
# 함수를 정의 한다.
# def 함수이름():
#     실행하고 싶은 명령들
#
# def 함수이름([매개변수]):
#     실행하고 싶은 명령들
#
# def 함수이름([가변매개변수]):
#     실행하고 싶은 명령들

# def print_greeting():
#     print("Hi Jake")
#     print("Good morning")
#     print("How are you")
#     print("Have a nice day")
#
# # 함수를 실행한다, 호출한다.
# print_greeting()

# 1. 처리만 있는 함수
# 함수를 실행하면 화면에 Hello World라는 글자를 출력한다.
def greeting():
    print("Hello World")
greeting()

# 2. 입력과 처리가 있는 함수
# 이름을 매개변수로 전달받아서 "Hi" + 이름을 화면에 출력한다.
# 매개변수를 어떻게 전달하고? 어떻게 받느냐?
def greeting(name):
    print("Hi", name)
greeting("Jake")

def greeting(name, age):
    print("Hi", name, "You are",age,"years old.")
greeting("Jake", 30)

# 3. 처리와 출력이 있는 함수
# 실행하면 랜덤한 정수 1개를 반환해주는 함수
import random
def make_random():
    return random.randint(1,10)

print(make_random())
random_number = make_random()

# 4. 입력 처리 출력이 있는 함수
# 숫자 두개를 입력받아서 두 숫자의 합을 반환하는 함수를 만든다.
def make_sum(number1, number2):
    total = number1 + number2
    return total

total = make_sum(11, 22)











