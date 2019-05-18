"""
판별문
if문은 판별문이다.
if문을 구성하는 키워드는 if, elif, else
if: 조건문이 참이라면 실행구문들을 실행한다. 딱 1번등장
elif: 그게아니라 만약 조건문이 참이라면 실행구문들을 실행한다. 0~무제한
else: 위에 조건들이 전부다 아니라면 실행구문들을 실행한다. 0,1 번 등장

if [조건문]:
    [실행구문들]
elif [조건문]:
    [실행구문들]
else [조건문]:
    [실행구문들]
"""

number = 5
if number > 5:
    print("숫자가 5보다 큽니다.")
elif number == 5:
    print("숫자가 5입니다.")
else:
    print("숫자가 5보다 크지 않습니다.")
"""
조건식이 뭐야?
조건식은 명제 -> 참과 거짓을 판별할 수 있는 문장
조건식은 결과가 Boolean 값(bool)이 나오는 것 : True, False

1) 비교 연산자
== 같다. a == b
!= 같지않다. a != b
> 크다 a > b
< 작다 a < b
>= 크거나 같다 a >= b ----> a => b (x)
<= 작거나 같다. a <= b
3 > 7

2) 값에 대해서
숫자 : 0은 False 나머지는 전부 True
문자 : ''은 False, 나머지는 전부 True
bool : False, True
None : False
리스트나 딕셔너리: [], {} False, 나머지는 True
[[]] : {공집합}  => True

"""


value = 1
bmi = 20.22

"""
18.5 미만: 저체중
18.5 이상 23 미만 : 정상체중
23 이상: 과체중
"""
"""
AND, OR, NOT
and : (a > b) and (b > c)
or : (a > b) or (b > c)
not: 
a = 0
if not a: => a가 비어있다면
    pass 

"""
