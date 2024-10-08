'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 함수활용
'''

def yak(num):
    list1 = []
    for i in range(1, num+1):
        if (num % i == 0):
            list1.append(i)
    return list1

num = int(input("숫자: "))
print(yak(num))