'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 함수활용
'''

def findAllLoc(strr, ch):
    mylist = []
    for i in range(len(strr)):
        if strr[i] == ch:
            mylist.append(i + 1)
    return mylist

strr = input("문자열: ")
ch = input("문자: ")
print(findAllLoc(strr, ch))