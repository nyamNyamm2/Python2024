'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 두 실수 입력받아 곱한 후 출력
'''

f1 = float(input("실수1: "))
f2 = float(input("실수2: "))
print(f1 * f2)



# 24.10.18 중간대비 복습
f1, f2 = map(float, input("실수 2개 입력: ").split())
print(f'{f1 * f2 :.2f}')