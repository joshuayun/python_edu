"""
연습문제 6. 퇴직 계산기
현재 나이와 퇴직을 하고 싶은 나이를 입력하면
올해로부터 계산하여 퇴직 연도를 출력하시오
입출력 예시 :
입력 화면 –
현재 나이를 입력하세요 : 20
퇴직을 원하는 나이를 입력하세요 : 50
출력 화면 –
당신은 앞으로 30 년 뒤에 퇴직을 하게 됩니다.
올해는 2019 년이므로 2049 년이 퇴직을 하는 해 입니다.
수치 계산과 날짜 계산이 필요합니다.
- datetime 을 사용하여 현재 년도를 알아내야 합니다.
"""
from datetime import datetime

while True:
    age = input("현재 나이를 입력하세요 : ")
    try:
        age = int(age)
        if age > 0:
            break
    except:
        print("현재 나이가 올바르지 않습니다. 재입력하세요.")
while True:
    retire_age = input("퇴직을 원하는 나이를 입력하세요 : ")
    try:
        retire_age = int(retire_age)
        if retire_age > 0:
            break
    except:
        print("퇴직 희망 나이가 올바르지 않습니다. 재입력하세요.")

age_gap = retire_age - age
now = datetime.now()
this_year = now.year
retire_year = this_year + age_gap
format_string = "당신은 앞으로 {} 년 뒤에 퇴직을 하게 됩니다.\n올해는 {} 년이므로 {} 년이 퇴직을 하는 해 입니다."
message_string = format_string.format(age_gap, this_year, retire_year)
print(message_string)