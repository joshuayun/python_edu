# 학생 5명의 성적을 입력받아서 평균과 총합을 구하는 코드
# 1) 5명이 아니라 입력값이 있는 동안 계속 성적 입력받기 : 반복문의 조건설정
# 2) 입력된 학생의 성적에서 최고점과 최저점을 찾아서 출력 하시오. : 최대 , 최소값 찾기
# - 최대, 최소값 찾으면서 진행
# - 모든 값을 저장해 둔 다음에 정렬해서 찾기:

# 변수의 초기화는 반복할 때마다 필요한 행위가 아니라면 반복문 밖에서 수행한다.
total_score = 0
avg_score = 0
student_count = 0
max_score = 0
min_score = 0

while True:
    print("____MENU____")
    print("1. 성적 입력하기")
    print("2. 합계와 평균 출력하기")
    print("3. 프로그램 종료하기")

    menu = input("메뉴를 선택하세요. : ")

    if menu == "1":
        while True:
            try :
                score = input("수학성적을 입력하세요.: ")
                score = int(score)
                student_count += 1
                # 제대로 입력이 완료되었다면 반복문은 종료한다.
                break
            except:
                print("성적은 숫자로만 입력하세요.")
        if(max_score < score):
            max_score = score
        if(min_score == 0):
            min_score = score
        if(min_score > score):
            min_score = score

        # 원래 변수 += 더할 값 : 원래 변수에 더할 값만큼 더해준다.
        total_score += score
    elif menu == "2":
        avg_score = total_score / student_count
        print("점수 합계:", total_score, "점수 평균:", avg_score, "최고점:", max_score, "최저점:", min_score)
    elif menu == "3":
        print("프로그램을 종료합니다.")
        exit()

