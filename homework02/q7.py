"""
연습문제 7. 직사각형 방의 면적
국제 표준단위인 피트/야드 단위로 입력받고 도량형을 변환하여 출력하시오.
방의 면적을 계산하여 출력하는 프로그램을 작성하시오. 방의 길이와 폭을 피트
단위로 입력받고, 제곱피트와 제곱미터로 면적을 나타내보시오.
입출력 예시 :
입력 화면 –
방의 길이는 몇 피트 입니까? 15
방의 너비는 몇 피트 입니까? 20
출력 화면 –
당신이 입력한 수치는 15, 20 피트입니다.
면적은
300 제곱 피트
27.871 제곱 미터
입니다.
추가 내용 :
제곱 미터 = 제곱 피트 * 0.09290304
입니다.
"""


while True:
    room_width = input("방의 길이는 몇 피트 입니까? :")
    try:
        room_width = int(room_width)
        if room_width > 0:
            break
    except:
        print("방의 길이가 올바르지 않습니다. 재입력하세요.")
while True:
    room_height = input("방의 너비는 몇 피트 입니까? :")
    try:
        room_height = int(room_height)
        if room_height > 0:
            break
    except:
        print("방의 너비가 올바르지 않습니다. 재입력하세요.")


room_area = room_width * room_height

room_area_meter = room_area * 0.09290304
room_area_meter = round(room_area_meter, 3)

format_string = "당신이 입력한 수치는 {}, {} 피트입니다.\n면적은\n{} 제곱 피트\n{} 제곱 미터\n입니다."
message_string = format_string.format(room_width, room_height, room_area, room_area_meter)
print(message_string)
