'''
실습일: 2024.10.15
실습자: 201910852 심기윤
실습내용: 파일에 임의의 글자 저장
'''

fileout = open("test.txt", "w", encoding="utf-8")
fileout.write("앙 기모취")
fileout.close()
