# 튜플
test_tuple = 1,2,3
test_tuple = (1,2,3)
# 튜플은 값이 비어있는 상태로 만들지 않는다.
# * 값 변경이 불가능하기 때문에

print(type(test_tuple))

# 값 갯수 알아보기
print(len(test_tuple))

# 리스트, 딕셔너리: 원하는 형태로 데이터를 저장하고 검색하는 등의 데이터를 다룰 때 필요하기 때문에 사용
# 튜플은 : 여러개의 값을 세트로 전달하고 싶을 때 *함수에서 사용하는 기법

def test_func():
    return 1,2,3

a = test_func()
print(a)

# 튜플은 unpack 이라는 기능이 있어서 여러개의 값을 한번에 전달하는데 사용된다.
# 언팩(unpack): 튜플 값을 여러개의 변수에 나누어 저장하는 것
a,b,c = test_func()
print(c)

# 언팩을 할 때 갯수를 알 수 없다면 마지막 변수앞에 *을 붙인다.
# *이 붙은 변수가 남은 모든 값을 리스트로 받아준다.
a,*b = test_func()
print(b)