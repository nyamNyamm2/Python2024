'''
실습일: 2024.10.15
실습자: 201910852 심기윤
실습내용: 파일에 쓰기 실습
'''

fileout = open("contact.txt", "w", encoding="utf-8")
fileout.write("앙기모취 010-1111-2222\n")
fileout.write("앙기모띠 010-3333-4444\n")
fileout.close()