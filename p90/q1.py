'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 함수활용
'''

def box(n, m):
    for i in range(n):
        for j in range(m):
            print('*', end=" ")
        print()

a = int(input("가로: "))
b = int(input("세로: "))
box(a, b)