'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 함수활용
'''

def summ(num):
    arr = []
    strr = str(num)
    size = len(strr)
    for i in range(size):
        arr.append(int(strr[i]))

    return sum(arr)

word = int(input("숫자: "))
hab = summ(word)
print(hab)