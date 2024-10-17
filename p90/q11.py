'''
실습일: 2024.10.17
실습자: 201910852 심기윤
실습내용: 함수의 활용
'''

def zegop(x, n):
    result = 1
    if n > 0:
        for i in range(n):
            result *= x
    elif n == 0:
        return result
    elif n < 0:
        for i in range(n, 0):
            result *= x
        result = 1/result

    return result

x, n = map(int, input("x와 n을 차례대로 입력: ").split())
print(zegop(x, n))
