'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 자료형 변환
'''

for i in range(1, 1001):
    strr = str(i)
    size = len(strr)
    if size == 1:
        print(i, ':', int(i))
    elif size == 2:
        sum = int(strr[0]) + int(strr[1])
        print(i, ':', sum)
    elif size == 3:
        sum = int(strr[0]) + int(strr[1]) + int(strr[2])
        print(i, ':', sum)
    else:
        print(i, ":", 1)
