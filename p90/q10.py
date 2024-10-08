'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 함수활용
'''

def cngF(c):
    return int((c * (9/5)) + 32)

c = int(input("섭씨: "))
print(cngF(c), 'F')