'''
실습일: 2024.10.15
실습자: 201910852 심기윤
실습내용: 파일 내용 매개변수의 글자만큼 읽기
'''

filein = open("./contact.txt", "r", encoding="utf-8")
readall = filein.read(8)
print(readall)
filein.close()