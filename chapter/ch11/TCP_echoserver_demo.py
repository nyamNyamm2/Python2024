'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 에코 서버 실습
'''

from socket import *

# 서버의 포트 번호 설정
port = 2500

# 클라이언트로 부터 받을 메시지의 크기 설정
BUFSIZE = 1024

# socket() 소켓 생성
sock = socket(AF_INET, SOCK_STREAM)

# bind() ip주소와 포트번호 지정 ip번호 공백이면 모든 클라이언트 허용
sock.bind(('', port))

# listen() 클라이언트 연결 대기 (listen () 안의 숫자는 연결 가능 클라이언트 수)
sock.listen(1)
print("클라이언트 대기중...")

# accept() 클라이언트 연결 수락 (c_sock은 새로운 소켓, (r_host, r_port)튜플은 클라이언트의 ip주소와 포트번호)
c_sock, (r_host, r_port) = sock.accept()
print(f'연결된 클라이언트: [ ip주소: {r_host} | 포트번호: {r_port} ]')

while True:
    # 클라이언트로 부터 데이터 수신
    # print("클라이언트 입력 대기중...")
    data = c_sock.recv(BUFSIZE)
    if not data:
        break
    print(f"받은 메시지: {data.decode()}")

    # 클라이언트로 데이터 송신
    c_sock.send(data)

c_sock.close()
