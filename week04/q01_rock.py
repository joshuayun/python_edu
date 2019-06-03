"""
가위바위보
유저가 가위, 바위, 보 중에 하나를 선택하면
컴퓨터도 가위, 바위, 보 중에 하나를 선택하고
이겼으면 승리
졌으면 패배 라고 출력
"""
import random
pattern = ['가위','바위','보']
user = '가위'

computer_index = random.randint(0,2)
computer = pattern[computer_index]

if user == computer:
    print("비겼습니다.")
elif user == '가위' and computer == '보':
    print("이겼습니다.")
elif user == '바위' and computer == '가위':
    print("이겼습니다.")
elif user == '보' and computer == '바위':
    print("이겼습니다.")
else:
    print("졌습니다.")









