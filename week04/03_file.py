"""
파일 다루기
1. 파일 열기 - 파일 사용권한 얻기
2. 파일 사용하기(쓰거나, 읽거나)
3. 파일 닫기 - 파일 사용권한 반납하기
"""
# 1. text 파일
# 1) 파일명 : 전체경로, 파일명
# 2) 모드 :
f = open("test.txt", "w", encoding='utf-8')

print("asdf","asdfasdf","asdf",file=f)
print("bbbb",file=f)

f.close()