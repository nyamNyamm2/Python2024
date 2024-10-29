'''
실습일: 2024.10.15
실습자: 201910852 심기윤
실습내용: 파일에 내용 추가하기
'''

fileout = open("contact.txt", "a", encoding="utf-8")
fileout.write("앙기모찌 010-5555-6666")
fileout.close()