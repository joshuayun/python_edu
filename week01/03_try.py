number = input("정수를 입력하세요. : ")

try:
    # 오류가 날지도 모르는 코드 작성
    number = int(number)
    print(number*2)
except:
    # 오류가 실제로 발생했다면 실행할 코드
    print ("숫자만 입력할 수 있습니다.")