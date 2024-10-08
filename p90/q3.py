'''
실습일: 2024.09.24
실습자: 201910852 심기윤
실습내용: 함수활용
'''

def findLoc(str1, str2):
    flag = -1
    n = max(len(str1), len(str2))
    for i in range(n):
        if str1[i] != str2[i]:
            flag = i
            break
    return flag+1

word1 = input("문자열1: ")
word2 = input("문자열2: ")
loc = findLoc(word1, word2)
print(loc)