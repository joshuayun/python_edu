"""
연습문제 5. 간단한 수학
두 개의 숫자를 입력받고, 두 숫자의 사칙연산 결과를 출력하시오.
입출력 예시 :
    입력 화면 – 첫번째 숫자를 입력 하세요 : 10 두번째 숫자를 입력 하세요  : 5
    출력 화면 –  10 + 5 = 15
                10 – 5 = 5
                10 * 5 = 50
                10 / 5 = 2
입력받아서 계산하는 문제입니다. - 문자 -> 숫자 변환을 기억하고 계셔야 합니다. - 가능하다면 특수 연산도 추가해보세요.
"""
try:
    number1 = input("첫번째 숫자를 입력 하세요 :")
    number1 = int(number1)
    number2 = input("두번째 숫자를 입력 하세요 :")
    number2 = int(number2)

    print("{} + {} = {}".format(number1, number2, number1 + number2))
    print("{} - {} = {}".format(number1, number2, number1 - number2))
    print("{} * {} = {}".format(number1, number2, number1 * number2))
    print("{} / {} = {}".format(number1, number2, number1 / number2))
    print("{} // {} = {}".format(number1, number2, number1 // number2))
    print("{} % {} = {}".format(number1, number2, number1 % number2))
    print("{} ^ {} = {}".format(number1, number2, number1 ** number2))

except:
    print("error. This program is terminated")