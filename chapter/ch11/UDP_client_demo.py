'''
실습일: 2024.11.12
실습자: 201910852 심기윤
실습내용: UDP 클라이언트 실습
'''

# 간단한 UDP 클라이언트 프로그램

import socket

# TCP와 동일
BUFFSIZE = 1024
port = 2500

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # TCP와 다르게 socket.SOCK_STREAM대신 DGRAM을 사용
msg = "Hello UDP server"
sock.sendto(msg.encode(),('localhost', port))               # send 대신 sendto 사용
data, addr = sock.recvfrom(BUFFSIZE)                        # recv 대신 recvfrom 사용
print(f"서버에서 받은 메시지: {data.decode()}")
