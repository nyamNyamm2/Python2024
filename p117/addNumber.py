'''
실습일: 2024.10.08
실습자: 201910852 심기윤
실습내용: 모듈 활용
'''

# addNumber.py

import sys

# 명령어 라인에서 받은 숫자들을 가져와서 합을 계산하는 함수
def add_numbers(numbers):
    total = 0
    for num in numbers:
        total += int(num)
    return total

if __name__ == "__main__":
# 프로그램 이름을 포함한 인자들을 받아옴
    args = sys.argv

# 첫 번째 인자는 스크립트의 이름이므로 제외하고 나머지를 숫자로 변환하여 합을 구함
    numbers = args[1:]

# 숫자들의 합을 계산
    result = add_numbers(numbers)

# 결과 출력
    print("입력한 숫자들의 합은:", result)