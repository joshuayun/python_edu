"""
input에 들어가는 안내 메시지만 매번 바뀌고
입력받는 처리 절차는 똑같은 경우에
사용할 수 있는 함수를 만든다.
"""
def input_with_message(msg, casting_func, error_msg):
    while True:
        value = input(msg)
        try:
            value = casting_func(value)
            break
        except:
            print(error_msg)
    return value

height = input_with_message("키를 입력하세요 :", float, "키를 잘못 입력하셨습니다.")
print("입력받은 키 값", height)
weight = input_with_message("체중을 입력하세요 :", float, "체중을 제대로 입력하세요.")
print("입력받은 체중 값", weight)





