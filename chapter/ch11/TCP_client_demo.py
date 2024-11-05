'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 에코 클라이언트 실습
'''

import socket

# 포트번호, 주소, 메시지 크기 설정
port = 2500
address = ('localhost', port)
BUFSIZE = 1024

# socket() 소켓 설정
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect() 서버 연결
s.connect(address)

while True:
    msg = input("서버로 보낼 메시지 입력: ")

    # 입력 메시지가 없을 경우 연결 종료
    if not msg.strip():
        break

    # 서버로 데이터 송신
    s.send(msg.encode())

    # 서버에서 데이터 수신
    r_msg = s.recv(BUFSIZE)

    # 서버로 부터 수신된 데이터가 없을 경우 연결 종료
    if not r_msg:
        break

    print("서버에서 보낸 메시지:", r_msg.decode())