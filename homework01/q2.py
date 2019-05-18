"""
연습문제 2.글자 수 세기
사용자에게 문자열을 입력받아 몇글자인지 카운트해서 출력하세요.
입출력 예시 :
    입력 화면 – String Input : Hello World
    출력 화면 – Hello World has 11 characters.
문자열을 다루기 위한 문제 입니다. 문자열의 글자 수를 카운트 하는데 여러가지 방법을 사용해보세요.
For 문으로 하셔도 되고, len 함수를 사용하셔도 좋습니다. 최대한 여러가지 방법으로 카운트 해보세요~!
"""

inputStr = input("카운트 할 문자열을 입력하세요. :")
inputStrCnt = len(inputStr)
print("1. len_funtion result: {} has {} characters.".format(inputStr, inputStrCnt))

inputList = list(inputStr)
inputListCnt = 0
for inputChar in inputList:
    inputListCnt = inputListCnt + 1

print("2. for result : {} has {} characters.".format(inputStr, inputListCnt))


