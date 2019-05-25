"""
연습문제 8. 피자 파티
피자를 정확하게 나누는 프로그램을 작성하세요. 사람 수, 피자 개수, 조각 개수를
입력받습니다. 이때 조각 개수는 짝수여야 합니다. 한 사람이 받게 되는 피자 고각
개수를 출력하고, 남는 피자 개수도 출력하시오.
입출력 예시 :
입력 화면 –
인원수를 입력하세요 : 8
피자 수를 입력하세요 : 2
한 피자당 조각 개수를 입력하세요 : 8
출력 화면 –
8 명이서 피자 2 개를 먹을 때
한명당 2 조각의 피자를 먹을 수 있습니다.
남는 조각은 0 개 입니다.
추가 내용 :
모든 입력은 숫자만 입력되어야 합니다. 숫자가 아닌 글자가 입력되면 다시 입력받도록
해보세요.
"""
while True:
    number_of_person = input("인원수를 입력하세요 : ")
    try:
        number_of_person = int(number_of_person)
        if number_of_person > 0:
            break
    except:
        print("인원수가 올바르지 않습니다. 다시 입력해 주세요.")
while True:
    number_of_pizza = input("피자수를 입력하세요 : ")
    try:
        number_of_pizza = int(number_of_pizza)
        if number_of_pizza > 0:
            break
    except:
        print("피자수가 올바르지 않습니다. 다시 입력해 주세요.")
while True:
    number_of_piece = input("한 피자당 조각 개수를 입력하세요 : ")
    try:
        number_of_piece = int(number_of_piece)
        if number_of_piece > 0:
            break
    except:
        print("한 피자당 조각 개수가 올바르지 않습니다. 다시 입력해 주세요.")

piece_of_persion = (number_of_pizza * number_of_piece) // number_of_person
number_of_extra_piece = (number_of_pizza * number_of_piece) % number_of_person

format_string = "{} 명이서 피자 {} 개를 먹을 때\n한명당 {} 조각의 피자를 먹을 수 있습니다.\n남는 조각은 {} 개 입니다."
message_string = format_string.format(number_of_person, number_of_pizza, piece_of_persion, number_of_extra_piece)
print(message_string)