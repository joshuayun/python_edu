"""
반복문은 같은 여러번 반복하여 입력하는 것이 비효율적이기 때문에
같은 코드를 반복실행할 때 사용하는 것
while ~ 동안
for 몇회
break : 만나는 즉시 break 를 감싸고 있는 가까운 반복문을 종료
continue: 만나는 즉시 그 이하의 구문은 실행하지 않고 반복문의 그다음 회차로 이동
"""
# number = 0
# while number <= 9:
#     number = number + 1
#     if number % 2 == 0:
#         continue
#     print(number)
#
# number = 0
# while number <= 9:
#     number = number + 1
#     if number % 2 != 0:
#         print(number)
#
# for [바구니에서 꺼낸 요소의 이름 in [바구니]:
#     [실행구문들]
# range : 범위생성자
# range(y) : 0 ~ (y-1)
# range(x,y) : x ~ (y-1)
# range(x,y,z) : x ~ (y-1) , z는 증감치
# 1~100 까지의 합을 구하기
total = 0
for number in range(1,101):
    total = total + number
print(total)

#1~100 사이의 홀수들의 합 구하기
odd_total = 0
for odd_number in range(1,101,2):
    odd_total = odd_total + odd_number
print(odd_total)


#1~100 사이의 짝수들의 합 구하기
even_total = 0
for even_number in range(2,101,2):
    even_total = even_total + even_number
print(even_total)

msg = "Hello World"
# len 바구니 형태에는 다 사용가능: len(바구니변수)
print(len(msg))

count = 0
for char in msg:
    count = count + 1
print(count)

# 바구니 객체 - 인덱스가 있는 변수
# 인덱싱 : 순번을 지정해서 해당 순번 위치에 있는 값만 꺼내보기 - 인덱스는 0부터 시작
# 슬라이싱 : x번부터 y번까지 일부만 꺼내보기
# 인덱싱과 슬라이싱은 -(마이너스) 도 가능하다.
# 변수[번호:] : 시작번호
# 변수[:번호] : 끝번호
# 변수[::번호] : 증감치
print(msg)
print(msg[-3])
print(msg[::-1])