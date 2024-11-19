'''
실습일: 2024.11.12
실습자: 201910852 심기윤
실습내용: TCP 파일 전송 실습 (수신 클라이언트)
'''

# 파일 수신 프로그램

import socket, os, sys

s_sock = socket.socket()
host = "localhost"
port = 2500

s_sock.connect((host, port))                        # 서버와 연결
s_sock.send("클라이언트 준비 완료".encode())                  # 준비 완료 메시지 송신
fn = s_sock.recv(1024).decode()                     # 경로를 포함한 파일이름 수신
filename = os.path.basename(fn)                     # 기본 파일이름 추출

with open('c:/temp/'+filename, 'wb') as f:          # 저장 파일 열기
    print('파일 열기')
    print('파일 받는 중')
    while True:
        data = s_sock.recv(8192)                    # 파일 내용 수신
        if not data:                                # 내용이 없으면 종료
            break
        f.write(data)                               # 내용을 파일에 쓰기

print('파일 다운로드 완료')
s_sock.close()
print('연결 종료')
