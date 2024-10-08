'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 판별식을 이용한 근의 종류 구하기
'''

a, b, c = map(int, input("ax*x + bx + c의 a, b, c를 입력: ").split())
D = b*b - 4*a*c
if D == 0:
    print(0)
elif D < 0:
    print("음수")
else:
    print("양수")