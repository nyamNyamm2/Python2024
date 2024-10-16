'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 최대 공약수 구하기
'''

a, b = map(int, input().split())

big = max(a, b)
small = min(a, b)

while small != 0:
    rest = big % small
    big = small
    small = rest

print(big)