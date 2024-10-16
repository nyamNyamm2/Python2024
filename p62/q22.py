'''
실습일: 2024.10.16
실습자: 201910852 심기윤
실습내용: 리스트 활용
'''

dlist= [1, 2, 3]
print(dlist)

dlist[1] = 17
print(dlist)

dlist2 = [4, 5, 6]
dlist.extend(dlist2)
print(dlist)

del(dlist[0])
print(dlist)

dlist.sort()
print(dlist)

dlist[3] = 25
print(dlist)
