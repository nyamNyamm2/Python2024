'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 파일 전송 실습 (송신 서버)
'''

# 파일 전송 프로그램

import socket
import os

# 소켓 설정
port = 2500
s_sock = socket.socket()
host = ""
s_sock.bind((host, port))
s_sock.listen(1)

print('연결 대기중...')
c_sock, addr = s_sock.accept()
print(f'{addr}과 연결됨')
msg = c_sock.recv(1024)
print(msg.decode())

try:
    while True:
        filename = input('전송할 파일 이름 입력(ex. c:/test/sample.bin): ')
        filename = filename.strip('"')

        if filename == '0':
            break
            
        if not os.path.exists(filename):
            print("파일이 존재하지 않습니다.")
            continue

        print(f"'{filename}' 전송 중")
        c_sock.sendall(filename.encode())  # 파일 이름 전송

        with open(filename, 'rb') as f:
            data = f.read(1024)  # 전송할 데이터 크기를 줄여줌
            while data:
                c_sock.sendall(data)
                data = f.read(1024)
        print('전송 완료')

        # 파일 전송 완료를 클라이언트에 알리는 신호
        c_sock.sendall(b"EOF")  # 예: "EOF" 신호로 전송 완료를 알림

except Exception as e:
    print(f"에러 발생: {e}")

finally:
    c_sock.close()
    s_sock.close()

print('연결 종료')