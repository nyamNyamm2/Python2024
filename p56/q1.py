'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 문자열 구분
'''

str = input("Your word: ")
loc = str.find('a')

if loc == -1:
    print("a가 들어간 단어를 입력하시오.")
else:
    print(str[:loc+1])
    print(str[loc+1:])