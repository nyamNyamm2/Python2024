'''
실습일: 2024.10.15
실습자: 201910852 심기윤
실습내용: 파일 내용 출력
'''

filein = open("test.txt", "r", encoding="utf-8")
readFile = filein.read()
filein.close()
print(readFile)