'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 조건에 따른 출력
'''

score = int(input("점수를 입력: "))
if score  < 70:
    print("불합격")
elif score >= 70:
    print("합격")
    if score >= 80:
        print("입학금면제 장학금")
        if score >= 90:
            print("등록금면제 장학금")