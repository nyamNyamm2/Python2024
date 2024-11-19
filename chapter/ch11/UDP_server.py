'''
실습일: 2024.11.12
실습자: 201910852 심기윤
실습내용: UDP 서버 실습
'''

# UDP 에코 서버 프로그램

import socket

# TCP와 동일
port = 2500
maxsize = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # UDP 소켓 (TCP에서 STREAM과 달리 DGRAM 사용)
sock.bind(('', port))
print("수신 대기 중")

# TCP와 달리 listen 사용x

while True:
    data, addr = sock.recvfrom(maxsize)                     # 데이터와 상대방 종단점 주소 수신 (TCP에서 recv대신 recvfrom 사용)
    print(f"받은 메시지: {data.decode()} ")
    print(f'연결된 클라리언트: {addr}')

    sock.sendto(data, addr)                                  # 재전송
