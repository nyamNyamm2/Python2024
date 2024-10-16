'''
실습일: 2024.10.16
실습자: 201910852 심기윤
실습내용: 문자열의 7번째 문자 판별
'''

strr = "hello"
if len(strr) >= 7:
    if strr[6].isalpha():
        print(strr[6])
else:
    print("문자가 없음")