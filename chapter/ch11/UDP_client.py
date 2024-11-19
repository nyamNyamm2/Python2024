'''
실습일: 2024.11.12
실습자: 201910852 심기윤
실습내용: UDP 클라이언트 실습
'''

# 간단한 UDP 클라이언트 프로그램

import socket
BUFFSIZE = 1024
port = 2500

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #UDP 소켓
msg = "Hello UDP server"
sock.sendto(msg.encode(),('localhost', port))           #메시지 전송

while True:
    data, addr = sock.recvfrom(BUFFSIZE)                #데이터 수신
    print(f"서버 응답: {data.decode()}")
    msg = input('보낼 메시지 입력: ')
    
    if msg == 'quit':
        break
        
    sock.sendto(msg.encode(), addr)                     #메시지 전송
print('연결 종료')
