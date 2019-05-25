"""
딕셔너리 : 사전형
값 한개 한개가 단어:뜻
"""

test_dict = {}
test_dict = dict()
# if test_dict => false
#test_dict {"단어":"뜻"}

# 인덱스가 있는 객체는 순서가 있다.
# 순서가 있는 객체는 인덱스가 있다.

# 인덱스가 없는 객체는 순서가 없다.
# 순서가 없는 객체는 인덱스가 없다.
# OrderedDict - 순서있는 딕셔너리

# 여러가지의 값을 여러개 담을 수 있다.
test_dict = {"apple":"red fruit", "banana":"yellow fruit", 0:"test number"}
# 딕셔너리는 key 값으로 접근한다.
# key:value
test_dict["apple"] = "my favorite fruit"

# 딕셔너리 키값에 숫자를 사용할 수 있지만
# 숫자를 사용한다고 해서 인덱스라고 생각해서는 안된다.
#test_dict = {0:"red fruit", 1:"yellow fruit", 2:"test number"}

# 삭제: del 은 대부분의 변수에 사용가능
# del(test_dict['apple'])

# 값 추가 하는법 : update(새로운 아이템)
test_dict.update({"새로운단어":"새로운뜻"})
print(test_dict)

# 값을 추가2: 새 키값에 바로 할당 - 더 많이 사용

test_dict['aaa'] = "bbb"
print(test_dict)
# 해당 키 값이 test_dict 에 존재하는지 확인
if 'aaa' in test_dict:
    test_dict.pop('aaa')
print(test_dict)

