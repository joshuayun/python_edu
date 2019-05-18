# 연산
# 1.산술연산 : 사칙연산, 특수연산
# 2.문자열연산 : + , *

name = "joshua"
msg = name # 실제로는 문자열 값이 복사되어 저장되지 않습니다. call by reference
msg = "Hello " + name
# 1) 문자열의 덧셈 : 문자열끼리 붙인다.

#print(msg) # Hello 이름

# 1. 인삿말을 입력하세요
# 2. 이름을 입력하세요
# 3. 인사말과 이름형태로 출력하는 프로그램 작성하세요.

"""
1. 입력 : 인삿말, 이름 - ex) 엑셀을 불러서
2. 저장 : 인삿말 greeting, 이름은 name
3. 처리 : 인삿말 + 이름 문자열 만들어서 msg 에 저장
4. 출력 : msg 변수의 값을 출력 - ex) pdf로 출력한다.
"""

# greeting = input("인삿말을 입력하세요.: ")
# name = input("이름을 입력하세요.: ")
# msg = greeting + " " + name
# print(msg)


# 2) 문자열의 곱셈: 문자열을 반복하여 붙인다.
# print("Hello"*7)
# 연산의 오버라이딩 : 내가 만든 데이터 타입에 연산을 정의할 수 있다.


# 산술연산 : 사칙연산
# 덧셈, 뺄셈, 곱셈, 나눗셈
number1 = 10
number2 = 7
number3 = number1 * number2

# 산술연산 : 특수연산
# **, % , //
# alt + shift + E
# number3 = number1 ** number2 # **은 거듭제곱 - 3**2 3의 2승
# print(number3)

# number3 = number1 % number2 # %는 나머지 - 정수 => 순서찾을떄 많이사용
# print(number3)

# number3 = number1 // number2 # // 몫 - 정수
# print(number3)

# 숫자 두개를 입력받아서 덧셈하여 출력하시오

# 1. 숫자 두개를 입력받는다.
# str: string 문자열
# int : integer 정수
# float : floating number 실수
# 문법 오류: 실행X, 오타나 실행문법 자체가 틀린 경우
# 논리 오류: 실행O, 결과가 엉망
# 런타임 오류: 실행O, 결과가 이상해지면서 프로그램이 종료

# ? : input 으로 입력을 받았더니 문자로 들어오네? 그럼 숫자로 어떻게 입력받지? 숫자로 입력받는 방법이 없다
# ? : 그럼 문자를 숫자로 바꿀수는 있나?
# 어떤 데이터를 다른 형태의 데이터로 바꾸는 것을 : Type Casting(형변환)


# num1 = input("첫번쨰 숫자를 입력하세요.:")
# num1 = int(num1)
# print(type(num1))
# num2 = input("두번쨰 숫자를 입력하세요.:")
# num2 = int(num2)
# print(type(num2))


#total = num1 + num2
# print(total)

# BMI 수치 구하기
# 신장과 체중을 입력받는다.
# 신장은 m 단위로 계산해야 한다.
# BMI = 체중 / 신장^2

# 1. 신장과 체중 입력받기 (변수에저장)
# 2. 형변환 - float
# 3. 신장을 m 단위로 변경
# 4. BMI 공식을 사용해서 계산
# 5. BMI 수치 출력
try:
    weight = input("체중를 입력하세요.(kg): ")
    weight = float(weight)

    height = input("신장을 입력하세요.(cm): ")
    height = float(height)
    height = height / 100

    bmi = weight / (height**2)
    bmi = round(bmi, 2)
    print("당신의 BMI:",bmi)
except:
    print("오류가 있어 프로그램이 종료합니다.")

# 연산자의 우선순위
# **
# *, / , % ,//
# +, -
# 연산자의 우선순위가 헷갈릴 수 있다. ()를 묶는다.

# 1) 여러명의 BMI 수치를 입력받아 계산하고 싶다. - 반복 => 반복문을 사용
# 2) BMI 수치를 판별해서 비만도를 출력하고 싶다. - 판별 => if, else
# 3) 오류 처리 - try - except


