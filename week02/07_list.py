"""
바구니 객체 - range()
바구니 객체 - 시퀀스객체(문자열, 리스트), 딕셔너리, 튜플, 셋
1) 만들기
2) 값 꺼내기
3) 값 변경하기
4) 값 추가하기
5) 값 삭제하기
"""
# 리스트
#test_list = [] # 비어있는 리스트
test_list = list()
test_list = [1,2,3,4,5]
#test_list = [1,"a",3.14,"hello"]
# 바구니 변수에는 여러 종류의 값들을 여러 개 저장할 수 있다.
print(test_list)
test_list[0] = 7
print(test_list)

# 리스트 값 추가하기
test_list.append(99)
print(test_list)
test_list.insert(0,1020)
print(test_list)
test_list.insert(99,1024) # 없는 인덱스를 사용할 때는 맨뒤로 붙는다.
test_list.insert(99,1024) # 없는 인덱스를 사용할 때는 맨뒤로 붙는다.
print(test_list)
test_list.insert(-3,2222) # -(마이너스)를 사용할 수 있다.
print(test_list)
test_list.insert(-99,333) #  마이너스는 갯수만큼만
print(test_list)

#remove는 값을 지운다. 동일한 값일 경우 맨앞에 값만 지운다. 없는 값 지우는 경우 오류

if 9090 in test_list:
    test_list.remove(9090)
    print(test_list)


print(test_list)
number = test_list.pop()
print(number)
print(test_list)

# 로또 번호 생성기 - 랜덤한 숫자 중복없이 뽑을떄 사용