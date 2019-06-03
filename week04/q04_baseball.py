"""
야구 게임
숫자 3개를 랜덤하게 생성 1~9 사의 수, 중복 X
3 9 4


사용자가 3개의 숫자를 입력하면
Strike : 숫자와 위치가 맞은 경우
Ball : 숫자만 맞은 경우
을 알려준다.

3 strike가 된 경우에만 맞았습니다.
게임을 종료

1. random
2. list
3. while문을 이용한 반복
4. 입력용 함수를 사용
"""
# 랜덤하게 3개 숫자 뽑기
import random
original_numbers = list(range(1,10))
numbers = random.sample(original_numbers, 3)
while True:
    user_numbers = []
    print("정답 숫자 3개를 입력하세요.")
    for _ in range(3):
        print("현재 입력된 수 ",user_numbers)
        number = input("숫자를 입력하세요 : ")
        user_numbers.append(int(number))
    print("입력한 정답 ", user_numbers)
    strike,ball = 0,0
    for index in range(3):
        if user_numbers[index] == numbers[index]:
            strike += 1
        elif user_numbers[index] in numbers:
            ball += 1
    print(f"{strike}S {ball}B")
    if strike == 3:
        print("정답입니다.")
        exit()








