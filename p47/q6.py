'''
실습일: 2024.09.10
실습자: 201910852 심기윤
실습내용: 대문자를 소문자로, 소문자를 대문자로 변환
'''

asc = ord(input("문자: "))

if asc >= 65 and asc <= 90:
    asc = asc + 32
elif asc >= 97 and asc <= 122:
    asc = asc - 32

print(chr(asc))