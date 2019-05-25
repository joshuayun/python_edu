"""
프로그래밍: random - 임의의 숫자를 뽑아내는 과정은 필수
 - 사용자의 비밀번호를 암호화 할 때
 - 데이터 분석을 할 때 임의의 데이터를 따로 추출해서 테스트 해보고 싶을 때
"""

# import 특정 모듈의 내용을 전부다 불러온다.
# 모듈: 특정 파일명, 특정 클래스명
import random

# 1. 일정 범위의 숫자를 랜덤하게 뽑기
random_number = random.randint(1,100) # range(x,y) x~y-1 but randit(x~y)

# 2. 숫자 3개를 랜덤하게 뽑아 보겠다.

"""
numbers = []
random_number = random.randint(1,100)
numbers.append(random_number)
random_number = random.randint(1,100)
numbers.append(random_number)
random_number = random.randint(1,100)
numbers.append(random_number)
print(numbers)
"""

# 랜덤뽑기는 :
# 1) 랜덤하게 생성
# 2) 원본에서 랜덤하게 뽑기
# 2-1) 원본을 랜덤하게 섞고, 순서대로 주기
# 2-2) 원본에서 랜덤하게 뽑아서 주기

# 1~45가 들어있는 원본
original_numbers = list(range(1, 46))

# 2-1) 원본 자체를 변경
random.shuffle(original_numbers)
# 섞인 원본에서 총 6개를 뽑아주면 된다.
print(original_numbers)


# 2-2) 바구니 객체가 주어졌을 때 원하는 갯수만큼 랜덤하게 요소를 뽑아주는 명령
# random
print(random.sample(original_numbers, 6))
