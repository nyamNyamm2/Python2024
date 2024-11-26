'''
실습일: 2024.11.19
실습자: 201910852 심기윤
실습내용: Threading 서버 실습
'''

#threading 모듈을 이용한 TCP 채팅 서버 프로그램

import socket
import threading

def handler(c, a):                          #데이터를 수신하여 처리하는 함수
    global connections
    c.setblocking(False)                    # Non-blocking 모드로 설정
    while True:
        try:
            data = c.recv(1024)
            if not data:                    #데이터가 없으면 연결이 종료된 것이므로 소켓 제거
                connections.remove(c)
                c.close()
                continue
        except:
            continue

        for connection in connections:
            try:
                if connection != c:
                    connection.send(data)   #모든 클라이언트에게 데이터 전송
            except:
                continue

# 소켓 설정
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 매핑
sock.bind(("", 2500))

# 소켓 연결
sock.listen(1)

# 연결된 클라이언트 목록
connections = [] #서버와 연결된 클라이언트 목록
print("서버 준비 완료")

while True:
    c_sock, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c_sock,a)) #서브스레드 생성
    cThread.daemon = True
    cThread.start()                                             #서브스레드 실행
    connections.append(c_sock)                                  # 새 클라이언트를 목록에 추가
    #print("연결된 클라이언트: ",connections)
    print("연결된 클라이언트: ",c_sock)