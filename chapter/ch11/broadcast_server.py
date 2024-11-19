'''
실습일: 2024.11.12
실습자: 201910852 심기윤
실습내용: 브로드 캐스트 서버 실습
'''

# 브로드캐스트 수신 프로그램

from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', 10000))

while True:
    msg, addr = s.recvfrom(1024)
    print(msg.decode())