numbers = list(range(1, 11))
print(numbers)

# for문의 목적: 바구니에서 하나씩 꺼내서 다루겠다.
# for 요소이름 in 바구니:
#   print (요소이름)

# for문은 바구니에서 하나씩 꺼내서 다 꺼낼때까지 반복하지만
# 다 꺼내고 나면 다시 넣어준다.
# for num in numbers:
#     print(num**2)
# print(numbers)


fruits = {"apple":2, "banana":7, "orange":1}
# 키 값만
for item in fruits:
    # apple
    print(item, fruits[item])

for item in fruits.keys():
    # apple
    print(item)

for item in fruits.values():
    # 2
    print(item)

# 키 밸류 둘다 튜플 형태로 꺼내준다.
for key,value in fruits.items():
    # apple,2
    print(key, value)