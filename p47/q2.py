'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: n! 구하기
'''

n = int(input("팩토리얼: "))
sum = 1
for i in range(1, n+1):
    sum = sum * i

print(sum)