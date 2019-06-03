"""
가위바위보
유저가 가위, 바위, 보 중에 하나를 선택하면
컴퓨터도 가위, 바위, 보 중에 하나를 선택하고
이겼으면 승리
졌으면 패배 라고 출력
"""
import random
pattern = ['가위','바위','보']

# 1. 가위 바위 보가 아닌 값 중에 종료 명령어 설정하기
# 2. 가위 바위 보가 한번 끝나도 프로그램이 종료되지 않기
# 3. 유저가 이긴 횟수, 진 횟수, 비긴 횟수 카운팅
win_count = 0
lose_count = 0
even_count = 0

while True:
    while True:
        print("* q를 입력하면 프로그램이 종료됩니다.")
        user = input("가위 바위 보 중에 한가지를 입력하세요 : ")
        if user in pattern:
            break
        elif user == 'q' or user == 'Q':
            exit()
        elif user.lower() == 'q':
            exit()
    user_index = pattern.index(user)
    computer_index = random.randint(0,2)
    computer = pattern[computer_index]
    print("유저 :",user,"컴퓨터 :", computer)
    if user_index == computer_index:
        even_count = even_count + 1
        # even_count += 1
        print("비겼습니다.")
    elif user_index == (computer_index+1)%3:
        win_count = win_count + 1
        # win_count += 1
        print("이겼습니다.")
    else:
        lose_count = lose_count + 1
        # lose_count += 1
        print("졌습니다.")
    print(f"승({win_count})/패({lose_count})/비김({even_count})")









