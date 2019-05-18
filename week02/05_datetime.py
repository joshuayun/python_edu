# 날짜 관련
# datetime 이라는 모듈
# 모듈: 하나 이상의 파이썬 파일이 있는 폴더
#import datetime.datetime       # A.B A폴더에 B라는 파일 혹은 클래스 혹은 함수
from datetime import datetime   # from A import B

now = datetime.now()            # 현재시각을 구해서 datetime 객체로 저장
#print(type(now))

# 올해가 윤년인지 판단하는 프로그램
this_year = now.year
# 어떤 해가 윤년인가?
# if문을 사용해서 올해가 윤년인지 판단하시오.
# 1) 연도가 4로 나누어 떨어지면 윤년
# 2) 연도가 100으로 나누어 떨어지면 윤년 X
# 3) 연도가 400으로 나누어 떨어지면 윤년

this_year = int(this_year)

leap_year=""
if this_year % 400 == 0 or (this_year % 100 != 0 and this_year % 4 == 0):
    leap_year = "윤년"
else:
    leap_year = "평년"


print("올해는 {} 입니다".format(leap_year))