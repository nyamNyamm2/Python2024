'''
실습일: 2024.10.22
이름: 201910852 심기윤
실습명: 자연수 n을 받아 n이하의 모든 숫자에 대해 콜라츠 추측 테스트
'''

def collatz(n):
    result = 0

    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        result += 1

    return result

n = int(input("콜라츠 추측을 테스트할 자연수 n을 입력하시오. >> "))

if n <= 1:
    print("콜라츠 추측을 테스트 할 수 없습니다.")
else:
    for i in range(n, 1, -1):
        print(f'n: {i}, result: {collatz(i)}')