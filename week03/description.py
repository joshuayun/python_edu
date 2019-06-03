"""
과제
자신만의 로또 예상 번호 생성기를 만들고
로또 5천원어치 구입
1. 예상 번호 캡처
2. 로또 복권사진
"""
while True:
    try:
        game_count = input("원하는 게임수를 입력하세요.: ")
        game_count = int(game_count)
        break
    except:
        print("게임수는 숫자로 입력하세요.")


