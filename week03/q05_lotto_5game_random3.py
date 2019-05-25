
import random
# 로또 5게임이 출력되도록 변경해 보세요.
while True:
    try:
        game_count = input("원하는 게임수를 입력하세요.: ")
        game_count = int(game_count)
        break
    except:
        print("게임수는 숫자로 입력하세요.")

# 숫자가 총 6개 되었을 때 까지만
for _ in range(game_count):
    # 새 게임을 뽑을 때마다 원본을 초기화
    original_numbers = list(range(1, 46))
    # 원본에서 내가 랜덤하게 뽑아낼 순번 0~44
    numbers = []
    # 원본에서 내가 랜덤하게 뽑아낼 순번
    for _ in range(6):
        # 첫 숫자를 뽑을 떄에는 총 갯수가 45개 , 0~44
        print("원본: ", original_numbers)
        print("현재 인덱스 끝번호:", len(original_numbers)-1)
        index = random.randint(0, len(original_numbers)-1)
        # 6개의 숫자를 중복 없이 뽑아주기
        number = original_numbers.pop(index)
        numbers.append(number)
        print("뽑은 수 :", number)
    print(sorted(numbers))
