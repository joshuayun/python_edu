
# 2-2) 바구니 객체가 주어졌을 때 원하는 갯수만큼 랜덤하게 요소를 뽑아주는 명령

import random
# 로또 5게임이 출력되도록 변경해 보세요.
while True:
    try:
        game_count = input("원하는 게임수를 입력하세요.: ")
        game_count = int(game_count)
        break
    except:
        print("게임수는 숫자로 입력하세요.")

original_numbers = list(range(1, 46))

# 숫자가 총 6개 되었을 때 까지만
for _ in range(game_count):
    numbers = random.sample(original_numbers, 6)
    print(sorted(numbers))
