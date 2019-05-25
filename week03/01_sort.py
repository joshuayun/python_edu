"""
정렬
"""
test_list = [7,4,99,54,20]

# sort, sorted
# sorted는 원본을 변경하지 않고, 정렬된 값을 만들어서 반환한다.
test_list2 = sorted(test_list)
print(test_list)
print(test_list2)

# sort() 는 원본을 변경하여 정렬한다.
# 원본을 변경하면 안되는 경우에는 sort()를 사용하지 않는다.
# 혹은 원본을 복제한 후에 sort() 사용한다.
test_list.sort()
print(test_list)

