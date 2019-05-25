# 숫자를 계속 입력받아서
# 입력받은 숫자들 중에 최댓값과 최솟값을 찾아서 출력하시오

# 입력받을 숫자들을 저장해둘 리스트
numbers = []
# 숫자를 무제한 받기 위한 while 문
while True:
    # 숫자 1번을 제대로 입력하기 위한 while 문
    while True:
        try:
            number = input("정수를 입력하세요.: ")
            if not number:
                break
            number = int(number)
            break
        except:
            print("정수만 입력하세요.")

    # 올바르게 입력된 숫자는 numbers에 저장한다.
    if not number:
        break
    numbers.append(number)

print(numbers)
# 입력된 값들을 오름차순으로 정렬
numbers.sort()
# 최댓값과 최소값 찾기
# 최댓값 : 마지막 numbers[-1]
# 최소값 : 처음 numbers[0]
print("최대값:", numbers[-1], "최소값:",numbers[0])


