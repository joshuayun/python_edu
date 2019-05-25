"""
바구니 객체: 한 변수 (저장공간)에 여러가지의 값을 여러개 한꺼번에 저장해 두는 역할
종류: 리스트, 딕셔너리, 튜플, 셋
바구니를 다루는 기법
1. 하나씩 꺼내서 다루는 법 - for
2. 원하는 요소를 선태갷서 다루는 법 : 인덱스 + 슬라이싱
"""
# * 빈 리스트는 if 에서 False가 나온다.
test_list = list()
test_list = []

""" 
- 리스트에 요소가 있으면 처리를 하겠다.
    if test_list:
        pass
- 리스트에 요소가 없으면 처리를 하겠다.
    if not test_list:
        pass
"""
test_list = []
# 변수에 처음으로 할당항하는 행위를 초기화

# 만약 1~10000까지 담겨있는 리스트를 만들어라
for number in range(1,10001):
    test_list.append(number)

test_list = range(1,10001) # range 10
test_list = list(range(1,10001)) # 리스트로 형변환 해서 넣어야함 - 보통 초기화할때 사용 (range -> list 형변환가능)

#index는 한글로 순번 - 순번은 0부터 시작한다.
print(test_list[3]) #리스트에서 값을 하나 선택해서 사용하려면 index를 사용한다.
test_list[3] = 7
# test_list.remove(100) # 해당값을 찾아서 삭제한다. 만약 동이랗ㄴ 값이 여러개 있을경우 맨처음에 나온 값 1개만 삭제된다.
if 100 in test_list:
    test_list.remove(100)

test_list.pop() # 맨 마지막 값을 꺼낸다.
index = 3
test_list.pop(index) # 해당위치의 값을 꺼낸다.

# 값을 추가하는 방법
# append
# insert

test_list.append(값) # 값을 맨끝에 추가한다.
test_list.insert(index, 값) #해당 값을 해당위치에 추가한다.
# 만약 해당하는 index가 없을 경우에는 맨 끝 혹은 맨 앞에 추가된다.