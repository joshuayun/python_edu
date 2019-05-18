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