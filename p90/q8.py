'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 함수활용
'''

def fac(n):
    gop = 1
    for i in range(1,n+1):
        gop *= i
    return gop

n = int(input("팩토리얼: "))
print(fac(n))
