'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 홀짝 판단
'''

user = int(input("정수 입력: "))
if user == 0:
    print(0)
elif user % 2 == 0:
    print("짝수")
else :
    print("홀수")


# 24.10.18 중간대비 복습
num = int(input("숫자 입력: "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")