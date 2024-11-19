'''
실습일: 2024.11.12
실습자: 201910852 심기윤
실습내용: 브로드 캐스트 클라이언트 실습
'''

# 브로드캐스트 송신 프로그램

from socket import *
#addr = ('192.168.0.255',10000) # 브로드캐스트 주소
addr = ('<broadcast>',10000) 

#브로드캐스팅을 위한 소켓 설정
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #브로드캐스트 옵션 설정

while True:
    smsg = input('전송할 메시지: ')
    s.sendto(smsg.encode(), (addr)) #브로드캐스팅 메시지 전송
