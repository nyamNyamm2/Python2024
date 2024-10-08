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