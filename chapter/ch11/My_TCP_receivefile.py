'''
실습일: 2024.11.12
실습자: 201910852 심기윤
실습내용: TCP 파일 전송 실습 (수신 클라이언트)
'''

# 파일 수신 프로그램

import socket
import os

s_sock = socket.socket()
host = "localhost"
port = 2500

s_sock.connect((host, port))  # 서버와 연결
s_sock.send("클라이언트 준비 완료".encode())  # 준비 완료 메시지 송신

while True:
    # 파일 이름 수신
    fn = s_sock.recv(1024).decode()
    if fn == "END":  # 서버에서 파일 전송이 끝났음을 알리면 종료
        print("모든 파일 다운로드 완료")
        break

    filename = os.path.basename(fn)  # 기본 파일 이름 추출
    save_path = 'c:/pyreceive/' + filename

    # 파일 저장을 위한 열기
    with open(save_path, 'wb') as f:
        print(f"'{filename}' 파일 받는 중")
        while True:
            data = s_sock.recv(8192)
            if data == b"EOF":  # 서버가 파일 전송을 마쳤음을 알림
                print(f"'{filename}' 파일 다운로드 완료")
                break
            f.write(data)

print("연결 종료")
s_sock.close()
