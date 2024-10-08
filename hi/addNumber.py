'''
실습일: 2024.10.08
실습자: 201910852 심기윤
실습내용: 모듈 활용
'''

# addNumber.py
import sys

def main():
    numbers = sys.argv[1:]

    total = sum(int(num) for num in numbers)
    print(f"입력된 숫자의 합: {total}")

if __name__ == "__main__":
    main()