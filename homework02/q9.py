"""
연습문제 9. 페인트 계산기
천장을 칠하는데 구매해야할 페인트의 양을 계산하시오.
1 리터로 칠할 수 있는 넓이는 9 제곱미터입니다.
10 제곱미터의 천장을 칠하려면 2 리터가 필요합니다.
(* 페인트는 무조건 1 리터 단위로 구매해야합니다.)
입출력 예시 :
입력 화면 –
칠할 천창의 넓이를 입력하세요 : 10
출력 화면 –
10 제곱미터의 천장을 칠하는데 2 리터의 페인터가 필요합니다.
추가 내용 :
모든 입력은 숫자만 입력되어야 합니다. 숫자가 아닌 글자가 입력되면 다시 입력받도록
해보세요.
출력값은 올림해서 정수단위로 출력되도록 하세요.
"""
import math

while True:
    try:
        ceil_width = input("칠할 천창의 넓이를 입력하세요 : ")
        ceil_width = int(ceil_width)
        if ceil_width > 0:
            break
    except:
        print("천장의 넓이가 올바르지 않습니다. 재입력하세요.")

paint = math.ceil(ceil_width / 9)


format_string = "{} 제곱미터의 천장을 칠하는데 {} 리터의 페인터가 필요합니다."
message_string = format_string.format(ceil_width, paint)
print(message_string)