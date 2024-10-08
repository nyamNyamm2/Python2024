'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 함수활용
'''

def find(num1, num2):
    return max(num1, num2)

num1 = int(input("숫자1: "))
num2 = int(input("숫자2: "))
print(find(num1, num2))