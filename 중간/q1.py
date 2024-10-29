'''
실습일: 2024.10.22
이름: 201910852 심기윤
실습명: 정수배열 받아 이웃한 쌍의 합이 소수인 경우 찾기
'''

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def find_prime_sum_pairs(arr):
    sum = 0
    for i in range(len(arr) - 1):
        sum = arr[i] + arr[i + 1]
        if is_prime(sum):
            print(f'({arr[i]}, {arr[i + 1]}) -> 합: {sum} (소수)')
        else:
            print(f'({arr[i]}, {arr[i + 1]}) -> 합: {sum} (소수 아님)')

intList = [2, 3, 5, 8, 13, 17]
find_prime_sum_pairs(intList)





