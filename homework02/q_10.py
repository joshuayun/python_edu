"""
연습문제 10. 셀프 계산대
간단한 셀프 계산대를 만들어 봅시다. 총 3 개의 제품을 구매하고 제품 가격 합계,
5.5%의 세금, 총액을 출력합니다. 각각의 물건을 구매할 때는 가격, 수량 순으로
입력받고 3 개의 제품에 대한 정보를 모두 입력 받으면 합계, 세금, 총액 순으로
출력하면 됩니다.
입출력 예시 :
입력 화면 –
첫번째 아이템 가격 : 25
첫번째 아이템 수량 : 2
두번째 아이템 가격 : 10
두번째 아이템 수량 : 1
세번째 아이템 가격 : 4
세번째 아이템 수량 : 1
출력 화면 –
중간 합계 : 64
세금 : 3.52
총 합계 : 67.52
"""
number_of_product = 3
price_of_preTax = 0
product = 0
for product in range(product, number_of_product):
    while True:
        price_of_item = input(str(product+1) + "번째 아이템 가격 : ")
        try:
            price_of_item = int(price_of_item)
            if price_of_item > 0:
                break
        except:
            print(str(product+1)+"번째 아이템 가격이 올바르지 않습니다. 다시 입력해 주세요.")

    while True:
        amount_of_item = input(str(product+1) + "번째 아이템 수량 : ")
        try:
            amount_of_item = int(amount_of_item)
            if amount_of_item > 0:
                break
        except:
            print(str(product+1)+"번째 아이템 수량이 올바르지 않습니다. 다시 입력해 주세요.")
    price_of_preTax = price_of_preTax + (price_of_item * amount_of_item)


tax = price_of_preTax * 5.5 / 100
price_of_total= price_of_preTax + tax

format_string = "중간 합계 : {}\n세금 : {:.2f}\n총 합계 : {:.2f}"
message_string = format_string.format(price_of_preTax, tax, price_of_total)
print(message_string)

