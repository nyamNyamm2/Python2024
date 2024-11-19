'''
실습일: 2024.11.12
실습자: 201910852 심기윤
실습내용: UDP 체팅 서버 실습
'''

# UDP 채팅 서버 프로그램

import socket

port = 2500
maxsize = 1024
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('', port))

print("클라이언트 대기중...")
while True:
    print("<- ", end ='')
    data, addr = sock.recvfrom(maxsize)
    print(data.decode())
    #print(addr)
    resp = input("-> ")
    sock.sendto(resp.encode(),addr)
