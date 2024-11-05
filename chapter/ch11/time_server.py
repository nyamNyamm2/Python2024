'''
실습일: 2024.11.05
실습자: 201910852 심기윤
실습내용: TCP 소켓 실습
'''

import socket
import time

# socket() 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 종단점(소켓이 사용할 ip주소와 포트번호의 조합) 지정
address = ('', 5000)    # ''은 모든 네트워크 인터페이스에서 연결 요청 허용, 로컬만 사용하려면 ip주소 입력 (ex.'192.168.0.0')

# bind() 소켓과 종단점 결합
sock.bind(address)

# listen() 클라이언트 연결 대기
sock.listen(5)

while True:
    
    # accept() 클라이언트 연결 수용
    client, addr = sock.accept()
    
    # 서버에 내용 출력
    print("Connection requested from", addr)
    
    # 클라이언트에게 메시지 전송 (실행방법: 터미널 -> telnet localhost 5000)
    client.send(time.ctime(time.time()).encode())
    
    # 소켓 종료
    client.close()

