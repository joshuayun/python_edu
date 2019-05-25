# 5명의 수학성적을 입력 받아서
# 평균과 총 합을 구하시오.
# 1. 5명의 수학성적 입력받기
# 2. 수학 성적들의 총합 구하기
# 3. 수학 성적들의 평균 구하기

# 1) 1명의 성적 입력받기
# 2) 2명의 성적 입력받기 + 총합과 평균 구하기
# 3) n명의 성적 입력받기
# 숫자로 제대로 입력할 때까지 계속 반복
total_score = 0
avg_score = 0


for _ in range(5):
    while True:
        try :
            score = input("수학성적을 입력하세요.: ")
            score = int(score)
            # 제대로 입력이 완료되었다면 반복문은 종료한다.
            break
        except:
            print("성적은 숫자로만 입력하세요.")
    # 원래 변수 += 더할 값 : 원래 변수에 더할 값만큼 더해준다.
    total_score += score


avg_score = total_score / 5

# +=, ==, *=, ./= : 복합할당 연산자
print("점수 합계:", total_score, "점수 평균:", avg_score)