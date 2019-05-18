"""
체중과 신장을 입력받고
BMI 수치를 계산하여 출력한다.
+ 과체중 여부를 판별하여 출력하시오.
"""

weight = input("체중을 입력하세요.: ")
height = input("신장을 입력하세요.: ")

try:
    weight = float(weight)
    height = float(height)
except:
    print("유효한 값이 아닙니다.")
    exit()

bmi = weight / (height / 100) ** 2
print(bmi)
"""
18.5 미만: 저체중
18.5 이상 23 미만 : 정상체중
23 이상: 과체중
"""
if bmi < 18.5:
    print("저체중")
elif (bmi >= 18.5) and (bmi < 23):
    print("정상체중")
else :
    print("과체중")

