'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 파일 전송 실습 (송신 서버)
'''

# 파일 전송 프로그램

import socket

# 소켓 설정
port = 2500                                                     # 포트번호
s_sock = socket.socket()                                        # 소켓 생성
host = ""                                                       # 클라 ip 주소
s_sock.bind((host, port))                                       # 바인딩
s_sock.listen(1)                                                # 동시 접속 1채널

print('연결 대기중...')

c_sock, addr = s_sock.accept()                                  #클라이언트와 연결
print(f'{addr}과 연결됨')
msg = c_sock.recv(1024)                                         #클라이언트로부터 준비 완료 수신
print(msg.decode())

filename = input('전송할 파일 이름 입력(ex. c:/test/sample.bin): ') #'\'대신 '/' 사용하여 경로 구분
filename = filename.strip('"')
print(f"'{filename} 전송 중'")

c_sock.sendall(filename.encode())                               #파일 이름 전송

with open(filename, 'rb') as f:
    #c_sock.sendfile(f,0) #파일 내용 전송

    data = f.read()
    while data:
        c_sock.sendall(data)
        data = f.read()

print('전송 완료')
c_sock.close()
