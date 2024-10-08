'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 문자열 리스트
'''

user = []
for i in range(5):
    user.append(input(""))

strr = ""
for i in range(5):
    if i < 4:
        strr += user[i] + "+"
    else:
        strr += user[i]

print(strr)