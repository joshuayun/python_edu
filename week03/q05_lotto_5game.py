
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
    numbers = []
    while len(numbers) < 6:
        number = random.randint(1, 45)
        if(not number in numbers):
            numbers.append(number)
    print(sorted(numbers))
