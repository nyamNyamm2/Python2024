'''
실습일: 2024.10.17
실습자: 201910852 심기윤
실습내용: 딕셔너리 활용
'''

days = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}

# 월 입력받고 일 출력하기
userMonth = input("월을 입력하시오: ").capitalize()
for i in days:
    if userMonth[:3] == i:
        print(f'{userMonth}(은)는 {days.get(i)}일까지 있음')

# 알파벳 순서대로 월 출력
klist = list(days.keys())
klist.sort()
print(klist)

# 일수가 31일인 월 모두 출력
vlist = []
for i in days:
    if days.get(i) == 31:
        vlist.append(i)
print(vlist)

# key-value쌍으로 출력
sortDays = sorted(days.items(), key=lambda x:x[1])
print(sortDays)