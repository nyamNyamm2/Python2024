'''
실습일: 2024.11.19
실습자: 201910852 심기윤
실습내용: GUI 서버 실습
'''

# 섭씨 온도를 받아 화씨 온도로 변환하여 전송하는 TCP 서버 프로그램

import sys
from socket import *

ECHO_PORT = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(eval(sys.argv[1]))
else:
    port = ECHO_PORT

# 소켓 설정
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', port))
s.listen(1)

print("클라이언트 연결 대기중...")
conn, (remotehost, remoteport) = s.accept()
print(f'연결된 클라이언트 [ IP주소: {remotehost} | 포트번호: {remoteport} ]')

while True:
    data = conn.recv(BUFSIZE)       # 데이터 수신
    if not data:                    # 연결이 종료되었음
        break
    data = float(data.decode())     # 수신 데이터를 float형으로 변환
    data = 9.0/5.0*data + 32.0      # 화씨 온도 계산
    data = '{:.1f}'.format(data)
    conn.send(data.encode())        # 화씨 온도 전송
    
conn.close()
