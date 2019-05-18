"""
연습문제	1. 인사말 출력하기
사용자의	이름을 입력받아 인사말을 출력하세요.
입출력 예시 :
    입력	화면	- What is your name? Jake
    출력화면 – Hello Jake! Glad to see you!
가장	기초가 되는 문제입니다. 입력과 출력에 신경써서	풀어보세요.
"""
try:
    name = input("What is your name? ")
    print("Hello {} ! Glad to see you!".format(name))
except:
    print("error. This program is terminated")