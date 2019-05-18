"""
format 명령어를 사용한 fotmat_string
돈! 123,411,234,234
"""
balance = 12341234
interest = 5
number_of_count = 4
number_of_year = 10
final_balance = balance * (1+interest/100/number_of_count)**(number_of_count*number_of_year)


"""
양식 문자열 만드는 순서
1. 예시 문자열을 만든다. bmi 수치는 22.05 이고 bmi 등급은 정상체중 입니다.
2. 예시 문자열에 값이 들어갈 자리를 만든다. - 양식 문자열
3. 만들어진 양식문자열에 값을 껴넣는다. - 출력 문자열 생성완료
"""
"""
.format의 옵션
{}: 자리 만들기
{0}: index를 써주면 입력된 값들 중 해당 위치의 값이 출력된다.
{:s} : 입력된 값의 타입을 지정하려면 :(콜론)을 찍고 그 뒤에 양식을 지정한다.
{0:f}
{:?f} : 양식 문자 앞에 숫자를 써서 숫자의 자릿수를 제한할 수 있다.
<>^ : 정렬 방향 결정
{:,d} : ,(콤마)를 사용하면 통화 단위처럼 표시할 수 있다.
s => 형식은 콤마(통화형식)로 표현할 수 없다.
"""

format_string = "원금이 {:15,d}원, 연이율 {:,.2f}%, 연지급횟수 {:,d}회인 예금에 {:,d}년 동안 예금을 해두면 최종 원리금 {:,.2f}원 입니다."
message_string = format_string.format(balance, interest, number_of_count, number_of_year, final_balance)
print(message_string)