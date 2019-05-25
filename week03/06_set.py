"""
셋: set - 집합
"""
test_set = {3,7,9,3,1,5,11,2,3}
print(test_set)
test_set.add(7)
print(test_set)
test_set.add(0.1)
print(test_set)

# 값을 삭제
# * 해당 값이 있으면 삭제한다.
# * 집합이기 때문에 중복값을 허용하지 않는다.
test_set.discard(7)
test_set.remove(3)
print(test_set)