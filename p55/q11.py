'''
실습일: 2024.10.16
실습자: 201910852 심기윤
실습내용: 문자열의 a를 e로 변경
'''

strr = "an americano is so dark and black"
print(f'변경 전: {strr}')

strr2 = ""
for i in range(len(strr)):
    if strr[i] == 'a':
        strr2 += 'e'
    else:
        strr2 += strr[i]
print(f'변경 후: {strr2}')