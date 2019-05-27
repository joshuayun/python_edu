import random

# 현재 프로그램을 변형해서
# 사용자가 입력한 갯수만큼 게임을 출력하는 프로그램을 작성하시오
# * 중복 게임이 존재하면 안됩니다.


# 셋에는 리스트나 딕셔너리 바구니 틀을 저장할 수 없기 때문에
games = list()

while True:
    try:
        game_count = input("게임수를 입력하세요.: ")
        game_count = int(game_count)
        break
    except:
        print("게임수를 숫자로 입력하세요.")

while len(games) < game_count:
    numbers = set()
    while len(numbers) < 6:
        number = random.randint(1, 45)
        numbers.add(number)

    # 현재 만들어진 게임을 games라는 리스트에 저장
    if numbers not in games:
        games.append(numbers)
print(games)