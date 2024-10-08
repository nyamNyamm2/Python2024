'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 소수 판별
'''

n = int(input("소수 판별: "))

for i in range (1, n+1):
    for j in range (2, i+1):
        if j == i:
            print(i)
        elif i % j == 0:
            break