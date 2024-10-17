'''
실습일: 2024.10.17
실습자: 201910852 심기윤
실습내용: 소수 판별
'''

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

cnt = 0

print("1부터 500까지 중 소수는 ", end = " ")
for i in range(1, 501):
    if isPrime(i):
        cnt += 1

        if cnt % 10 == 0:
            print()
        print(i, end = ", ")
