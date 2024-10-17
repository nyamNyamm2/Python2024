'''
실습일: 2024.10.17
실습자: 201910852 심기윤
실습내용: 딕셔너리 활용
'''

d = [ {'name' : 'Kim', 'phone' : '567-1414', 'email' : 'Kim@daum.net'},
      {'name' : 'Lee', 'phone' : '234-5678', 'email' : 'lee@naver.com'},
      {'name' : 'Park', 'phone' : '555-9876', 'email' : ''} ]

# 전화번호가 8로 끝나는 사용자 이름 출력
for dic in d:
    phone = dic['phone']
    if phone[len(phone)-1 : ] == '8':
        print(dic['name'])

# 이메일이 없는 사용자의 이름 출력
for dic in d:
    if dic['email'] == '':
        print(dic['name'])

# 사용자의 이름을 입력받아 정보를 출력하고 이름 부재시 이름 없다고 출력
name = input("이름: ").capitalize()
flag = 0

for dic in d:
    if dic['name'] == name:
        print(f'{dic['name']}의 전화번호는 {dic['phone']}, 이메일은 {dic["email"]}입니다.')
        flag = 1

if flag == 0:
    print(f'찾으시는 사용자 {name}의 정보가 존재하지 않습니다.')