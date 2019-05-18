"""
체중과 신장을 입력받고
BMI 수치를 계산하여 출력한다.
+ 과체중 여부를 판별하여 출력하시오.
"""

while True:
    weight = input("체중을 입력하세요.: ")
    try:
        weight = float(weight)
        if weight > 0:
            break
    except:
        print("입력값이 올바르지 않습니다.")

while True:
    height = input("신장을 입력하세요.: ")
    try:
        height = float(height)
        if height > 0:
            break
    except:
        print("입력값이 올바르지 않습니다.")

bmi = weight / (height / 100) ** 2

"""
bmi 판별
18.5 미만: 저체중
18.5 이상 23 미만 : 정상체중
23 이상: 과체중
"""

"""
String a;
a = "";
타입의 명시적 선언
"""
# 변수의 선언, 변수의 초기화가 동시에 해야만 합니다.
# 타입의 암시적(묵시적) 선언
bmi_level = ""
"""
데이터 타입을 쓰는 언어들에 강타입, 약타입
* 파이썬으로 프로그래밍 할 때도 타입을 지정해서 쓰는 경우도 있다.
"""

if bmi < 18.5:
    bmi_level = "저체중"
elif (bmi >= 18.5) and (bmi < 23):
# bmi 18.5<= bmi <23 #chaining comparison 요것도 됨
    bmi_level = "정상체중"
else :
    bmi_level = "과체중"

format_string = "bmi 수치는 %0.2f 이고 bmi 등급은 %s 입니다."
msg_string = format_string % (bmi, bmi_level)
print(msg_string)

"""
if 조건1 and 조건2 : 조건1이 거짓이라면 조건2는 판별하지 않는다.
if 조건1 or 조건2 : 조건1이 참이라면 조건2는 판별하지 않는다.
"""



