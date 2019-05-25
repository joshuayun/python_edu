
# 2-1) 원본 자체를 변경

import random
# 로또 5게임이 출력되도록 변경해 보세요.
while True:
    try:
        game_count = input("원하는 게임수를 입력하세요.: ")
        game_count = int(game_count)
        break
    except:
        print("게임수는 숫자로 입력하세요.")

orginal_numbers = list(range(1, 46))
# 숫자가 총 6개 되었을 때 까지만

"""
시퀀스 객체 : 순서대로 들어가 있는 애들
하나의 요소만 골라내는 방법: 인덱싱 orginal_number[3]
끊어내는 방법: 슬라이싱 : orginal_numbers[2:4]
"""
for _ in range(game_count):
    random.shuffle(orginal_numbers)
    # 슬라이싱은 뺴내는 것은 아니다.
    # 슬라이싱을 해서 고른 요소들은 복사해서 돌려준다.
    numbers = orginal_numbers[:6]
    print(sorted(numbers, reverse=True))
#. sort 의 reverse 옵션은 정렬의 오름차순을 내림차순으로 변경하는것이고,
# revered() 함수는 리스트에 잇는 순서 자체를 반대로 바꾸는것이다.