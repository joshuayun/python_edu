"""
학생의 이름과 국어,영어,수학 점수를 입력받아서 저장 후
이름을 검색하면 해당 학생의 국어,영어,수학 점수를 출력하세요.
"""
"""
리스트와 딕셔너리: 자료구조
자료를 저장하고, 검색하고 변경하기 용이하기 때문
"""

# 1) 학생의 이름 입력받기
# 2) 학생의 성적, 국영수 입력받기
# 3) 학생의 이름으로 검색하기
# * 어떤 형식으로 자료를 저장할 것이냐?
"""
{
    "홍길동":{"국어":100, "수학":80, "영어":95},
    "강호동":{"국어":90, "수학":82, "영어":70},
    "김희철":{"국어":70, "수학":70, "영어":100}
}
"""
student_scores = {}
# 1. 성적입력
# 2. 학생 이름으로 성적입력
while True:
    print("___MENU___")
    print("1. 성적 입력")
    print("2. 학생 검색")
    print("3. 프로그램 종료")
    menu = input("메뉴를 선택하세요.: ")
    if menu == "1":
        # 학생 무제한 입력받기, 학생의 이름을 입력하지 않으면 종료
        while True:
            # 학생의 이름 입력받기
            name = input("학생 이름: ")
            if not name:
                break
            # 국영수 성적 입력받기
            korean = input("국어 점수: ")
            korean = float(korean)
            math = input("수학 점수: ")
            math = float(math)
            english = input("영어 점수: ")
            english = float(english)
            # 입력받은 데이터를 저장하기
            student_scores[name] = {"국어":korean, "수학":math, "영어":english}

        total_korean = 0
        total_math = 0
        total_english = 0
        for score in student_scores.values():
            total_korean += score["국어"]
            total_math += score["수학"]
            total_english += score["영어"]

        # 평균 출력하기
        student_count = len(student_scores) # 총 학생수
        print(total_korean/student_count, total_math/student_count, total_english/student_count)

    elif menu == "2":
        name = input("검색하고 싶은 학생의 이름:")
        if name in student_scores:
            print(name,"학생의 성적")
            print(student_scores[name])
        else:
            print("해당 학생이 존재하지 않습니다.")
    elif menu == "3":
        print("프로그램을 종료합니다.")
        exit()
    else:
        print("없는 메뉴 입니다.")
