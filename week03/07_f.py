"""
f_문법
f_string

"""

"""
양식 문자열 만드는 방법
1) % 문법
2) format 문법
3) f string

양식 문자열 만드는 순서
1) 원하는 예시 문장 쓰기
2) 채울 자리 만들기
3) 완성된 문자열 변수에 저장하기
"""
name = "홍길동"
final_balance = 12341234.222
# 소수점 둘째자리까지 출력
# 통화 단위로 표시되게 변경하시요.
format_string = f"{name:>10s}님의 최종 원리금은 {final_balance:10,.2f}원 입니다."
print(format_string)