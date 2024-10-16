'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 윤년 계산
'''

cnt = 0
sum = 0

print("2000년 부터 2500년까지 윤년인 해")

for i in range(2000, 2501):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        if cnt == 10:
            cnt = 0
            print()
        print(i, end="년 ")
        cnt += 1
        sum += 1
print(f'\n2000년 부터 2500년까지 윤년인 해의 개수는 {sum}개 입니다.')
