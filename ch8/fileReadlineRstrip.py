'''
실습일: 2024.10.15
실습자: 201910852 심기윤
실습내용: 파일에서 마지막 줄바꿈 기호 삭제하고 읽기
'''

filein = open("./contact.txt", "r", encoding="utf-8")
readLine = filein.readline().rstrip()
while readLine != "" :
    print(readLine)
    readLine = filein.readline().rstrip()
filein.close()