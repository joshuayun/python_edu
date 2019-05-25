
# * 랜덤으로 뽑았을 때 어떻게 겹치지 않게 뽑을 것인가?
# 로또 예상 번호 만들기
# 1~ 45 사이의 정수들 중에서 겹치지 않게 6개의 숫자로 1게임 구성됨
# 로또 용지 1장에는 총 5게임까지 쓸 수 있습니다.
# 게임끼리는 중복이 허용

# 1게임 만들어 내기
# 1) random 모듈을 사용해서 랜덤한 숫자 1개 만들기
# 2) 중복된 값이 없다면 이것을 숫자 리스트에 집어 넣기
# 3) 숫자 리스트에 총 6개의 숫자가 등록이 되었다면 뽑기 종료
import random

numbers = []

# 숫자가 총 6개 되었을 때 까지만
"""
while True:
    number = random.randint(1, 45)
    if(not number in numbers):
        numbers.append(number)
    if len(numbers) == 6:
        break
"""
while len(numbers) < 6:
    number = random.randint(1, 45)
    if(not number in numbers):
        numbers.append(number)
print(sorted(numbers))
